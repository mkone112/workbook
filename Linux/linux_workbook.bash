dfn
#менеджер пакетов fedora
zypper
#менеджер пакетов openSUSE


dstat --disk-util -D sda > /tmp/dst.txt &
watch -t "tail -2 /tmp/dst.txt | tail -1"

~/.bashrc
    # for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
    HISTSIZE=1000
    HISTFILESIZE=2000


sudo chown -R -v $USER:$USER /mnt


копирование с сохранением всех атрибутов
    cp -a <source> <target>
    проверяем:
    diff <(getfacl -R folder1) <(getfacl -R folder2)


отключить пробуждение
grep . /sys/bus/usb/devices/*/power/wakeup
cat /proc/acpi/wakeup | grep enabled
sudo nano /etc/systemd/system/disable-wakeup.service
[Unit]
Description=Disable wakeup triggers

[Service]
Type=oneshot
ExecStart=/bin/sh -c "echo 'disabled' > /sys/bus/usb/devices/1-5/power/wakeup; echo 'disabled' > /sys/bus/usb/devices/1-6/power/wakeup; echo XHC > /proc/acpi/wakeup; echo PEG0 > /proc/acpi/wakeup; echo GLAN > /proc/acpi/wakeup"
ExecStop=/bin/sh -c "echo 'disabled' > /sys/bus/usb/devices/1-5/power/wakeup; echo 'disabled' > /sys/bus/usb/devices/1-6/power/wakeup; echo XHC > /proc/acpi/wakeup; echo PEG0 > /proc/acpi/wakeup; echo GLAN > /proc/acpi/wakeup"
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
# При изменениях сервиса - может потребоваться обновить файл(симлинк?)
systemctl daemon-reload


cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors
sudo cpupower frequency-set -g performance
sudo systemctl enable cpupower.service


sudo nano /usr/share/applications/konqbrowser.desktop
    Icon=system-file-manager

zsh by default
    sudo pacman -Sy zsh
    sudo chsh -s /bin/zsh root
    sudo chsh -s /bin/zsh $USER
    sudo cat ./.bash_history > $HISTFILE

bash|(while read;do printf "%80s\n" $REPLY;done)
printf "%*s\n" $(((${#REPLY}+$COLUMNS)/2)) $REPLY

bash|(while read;do printf "%*s\n" $(((${#REPLY}+$COLUMNS)/2)) $REPLY;done)


display_center(){
    columns="$(tput cols)"
    while IFS= read -r line; do
        printf "%*s\n" $(( (${#line} + columns) / 2)) "$line"
    done < "$1"
}
bash


print_center(){
    local x
    local y
    text="$*"
    x=$(( ($(tput cols) - ${#text}) / 2))
    echo -ne "\E[6n";read -sdR y; y=$(echo -ne "${y#*[}" | cut -d';' -f1)
    echo -ne "\033[${y};${x}f$*\n"
}
print_center(){
    local x
    local y
    while read; do
        x=$(( ($(tput cols) - ${#REPLY}) / 2))
        echo -ne "\E[6n";read -sdR y; y=$(echo -ne "${y#*[}" | cut -d';' -f1)
        echo -ne "\033[${y};${x}f$*\n"
    done
}
# рабочая центровка
center()
{

     value="$*"
     if [[ "${#value}" -lt $COLUMNS ]] ; then
       width=$(( (  $COLUMNS - ${#value} ) / 2 ))
       printf "%${width}s\n"  "$1"
     else
        echo "$1"
     fi
}
bash|(while read;do center "${REPLY}";done;echo -n "")
bash|(while read;do echo $REPLY|sed  -e :a -e 's/^.\{1,77\}$/ & /;ta';done)


center()
{
  mylen=$(( ${#1}/2 ))
  [ ${#1} -ne $((${mylen}*2)) ] && mylen=$((${mylen}+1))
  myalign=$(( ${COLUMNS}/2 + ${mylen} ))
  printf "%${myalign}s\n" "${1}"
}
bash|(while read;do center "${REPLY}";done)