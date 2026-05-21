#!/bin/bash
# XmindAnything Dependency Setup
# 自动检测并安装缺失的依赖，支持 apt / pip / npm
# Usage: bash scripts/setup.sh          # interactive (prompts before install)
#        bash scripts/setup.sh --fix    # auto-install without prompting

set -uo pipefail

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'
INSTALL_MODE="${1:-prompt}"  # prompt | fix
MISSING=()

echo "================================================"
echo "  XmindAnything Dependency Check"
echo "================================================"

check_cmd() {
    if command -v "$1" &>/dev/null; then
        echo -e "  ${GREEN}✅${NC} $1"
    else
        echo -e "  ${RED}❌${NC} $1 (missing)${NC}"
        MISSING+=("cmd:$1")
    fi
}

check_pip() {
    if python3 -c "import $1" 2>/dev/null; then
        echo -e "  ${GREEN}✅${NC} pip:$1"
    else
        echo -e "  ${RED}❌${NC} pip:$1 (missing)${NC}"
        MISSING+=("pip:$1")
    fi
}

check_apt() {
    if dpkg -l "$1" 2>/dev/null | grep -q '^ii'; then
        echo -e "  ${GREEN}✅${NC} apt:$1"
    else
        echo -e "  ${RED}❌${NC} apt:$1 (missing)${NC}"
        MISSING+=("apt:$1")
    fi
}

# ── Core ──
echo -e "\n${GREEN}[Core]${NC}"
check_cmd xmindmark

# ── System (apt) ──
echo -e "\n${GREEN}[System / apt]${NC}"
check_apt poppler-utils
check_apt tesseract-ocr
check_apt tesseract-ocr-chi-sim
check_cmd tesseract
if ! command -v soffice &>/dev/null; then
    check_apt libreoffice-impress-nogui
fi

# ── Python (pip) ──
echo -e "\n${GREEN}[Python / pip]${NC}"
check_pip docx
check_pip pptx
check_pip openpyxl

# ── Upload ──
echo -e "\n${GREEN}[Upload]${NC}"
check_cmd curl

# ── Cleaning ──
echo -e "\n${GREEN}[Content Cleaning]${NC}"
check_cmd python3

# ── Summary ──
echo ""
if [ ${#MISSING[@]} -eq 0 ]; then
    echo -e "${GREEN}================================================${NC}"
    echo -e "${GREEN}  ✅ All dependencies ready!${NC}"
    echo -e "${GREEN}================================================${NC}"
    exit 0
fi

echo -e "${YELLOW}────────────────────────────────────────────────${NC}"
echo -e "${YELLOW}  ${#MISSING[@]} dependency(s) missing:${NC}"
for dep in "${MISSING[@]}"; do
    echo -e "${YELLOW}    - $dep${NC}"
done
echo -e "${YELLOW}────────────────────────────────────────────────${NC}"

SHOULD_INSTALL=false
if [ "$INSTALL_MODE" = "fix" ]; then
    SHOULD_INSTALL=true
else
    echo ""
    read -rp "Auto-install missing dependencies? [Y/n] " ans
    if [ "$ans" != "n" ] && [ "$ans" != "N" ]; then
        SHOULD_INSTALL=true
    fi
fi

if ! $SHOULD_INSTALL; then
    echo -e "${YELLOW}Skipped. Manually install: bash scripts/setup.sh --fix${NC}"
    exit 1
fi

# ── Install ──
echo -e "\n${GREEN}[Installing...]${NC}"
SUCCESS=true

for dep in "${MISSING[@]}"; do
    type="${dep%%:*}"
    name="${dep#*:}"
    case "$type" in
        apt)
            echo "  → apt install $name"
            apt-get install -y "$name" 2>/dev/null || { echo "  ⚠️ failed: $name"; SUCCESS=false; }
            ;;
        cmd)
            case "$name" in
                xmindmark)
                    echo "  → npm install -g xmindmark"
                    npm install -g xmindmark 2>/dev/null || { echo "  ⚠️ failed: $name"; SUCCESS=false; }
                    ;;
                *) echo "  ⚠️ unknown cmd: $name"; SUCCESS=false; ;;
            esac
            ;;
        pip)
            echo "  → pip install $name"
            pip3 install --break-system-packages "$name" 2>/dev/null || { echo "  ⚠️ failed: $name"; SUCCESS=false; }
            ;;
    esac
done

if $SUCCESS; then
    echo -e "\n${GREEN}✅ All dependencies installed successfully!${NC}"
else
    echo -e "\n${YELLOW}⚠️ Some dependencies may not have installed correctly.${NC}"
    echo -e "${YELLOW}  Run again: bash scripts/setup.sh${NC}"
fi
