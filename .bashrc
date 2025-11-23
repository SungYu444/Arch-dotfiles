#
# ~/.bashrc
#

fastfetch --logo ~/Wallpaper/ascii-art1.png

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

export PATH="/home/yu/.local/bin:$PATH"

