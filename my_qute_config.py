# qutemacs - a simple, preconfigured Emacs binding set for qutebrowser
#
# The aim of this binding set is not to provide bindings for absolutely
# everything, but to provide a stable launching point for people to make their
# own bindings.
#
# Installation:
#
# 1. Copy this file or add this repo as a submodule to your dotfiles.
# 2. Add this line to your config.py, and point the path to this file:
# config.source('qutemacs/qutemacs.py')


config = config  # type: ConfigAPI # noqa: F821 pylint: disable=E0602,C0103
c = c  # type: ConfigContainer # noqa: F821 pylint: disable=E0602,C0103

config.load_autoconfig()

# c.input.insert_mode.auto_enter = False
# c.input.insert_mode.auto_leave = False
c.input.insert_mode.plugins = True
c.input.insert_mode.auto_load = True

# Forward unbound keys
c.input.forward_unbound_keys = "all"

# Change home page
c.url.start_pages = ["https://www.google.com"]

c.url.searchengines = {
    'DEFAULT': 'https://www.google.com/search?q={}',
    'du': 'https://duckduckgo.com/?q={}',
    'bi': 'https://www.bing.com/?{}',
    'yt': 'https://www.youtube.com/results?search_query={}',
    'wk': 'https://tr.wikipedia.org/wiki/{}',
    'ya': 'https://yandex.com.tr/search/?text={}',
    'am': 'https://www.amazon.com.tr/s?k={}',
    'hoog': 'https://hoogle.haskell.org/?hoogle={}'
}

ESC_BIND = 'clear-keychain ;; search ;; fullscreen --leave'


# ** Media
c.content.autoplay = False

#config.bind('p', 'mode-enter caret')

c.bindings.default['normal'] = {}
# Bindings
c.bindings.commands['normal'] = {
    '<j>': 'mode-enter caret',
    # Navigation
    '<ctrl-v>': 'scroll-page 0 0.9',
    '<alt-v>': 'scroll-page 0 -0.9',
    '<alt-z>': 'scroll top',
    '<alt-shift-z>': 'scroll bottom',
    # '<Backspace>': 'scroll-page 0 -0.9',
    # '<Space>': 'scroll-page 0 0.9',

    # Commands
    '<alt-x>': 'set-cmd-text :',
    '<ctrl-x><ctrl-c>': 'quit',

    # searching
    '<ctrl-s>': 'set-cmd-text /',
    '<ctrl-r>': 'set-cmd-text ?',

    # hinting
    '<f>': 'hint all',
    '<ctrl-u><f>': 'hint all hover',
    '<shift-t>': 'hint all tab-bg',
    '<t>': 'hint all tab-fg',
    '<w><l>': 'hint all yank-primary',
    '<w><w>': 'yank url',
    '<d>': 'yank all download',

    # history
    '<shift-f>': 'forward',
    '<shift-b>': 'back',
    '<ctrl-c><ctrl-f>': 'forward',
    '<ctrl-c><ctrl-b>': 'back',
    '<shift-h>': 'history',

    # bookmarks
    '<shift-m>': 'bookmark-add',
    '<ctrl-m>': 'open qute://bookmarks',


    # tabs
    '<ctrl-tab>': 'tab-next',
    '<ctrl-shift-tab>': 'tab-prev',
    '<alt-n>': 'tab-next',
    '<shift-alt-n>': 'tab-move +',
    '<alt-p>': 'tab-prev',
    '<shift-alt-p>': 'tab-move -',
    '<ctrl-x><b>': 'set-cmd-text -s :tab-focus',
    '<ctrl-x><k>': 'tab-close',
    '<ctrl-c><p>': 'tab-pin',
    '<ctrl-c><m>': 'tab-mute',
    '<ctrl-x><0>': 'tab-close',
    '<ctrl-x><1>': 'tab-only',
    '<Alt-1>': 'tab-focus 1',
    '<Alt-2>': 'tab-focus 2',
    '<Alt-3>': 'tab-focus 3',
    '<Alt-4>': 'tab-focus 4',
    '<Alt-5>': 'tab-focus 5',
    '<Alt-6>': 'tab-focus 6',
    '<Alt-7>': 'tab-focus 7',
    '<Alt-8>': 'tab-focus 8',
    '<Alt-9>': 'tab-focus -1',

    # frames
    '<ctrl-x><5><0>': 'close',
    '<ctrl-x><5><1>': 'window-only',
    '<ctrl-x><5><2>': 'set-cmd-text -s :open -w',
    '<ctrl-u><ctrl-x><5><2> ': 'set-cmd-text -s :open -p',


    # open links
    '<g>': 'set-cmd-text -s :open',
    '<shift-g>': 'set-cmd-text -s :open -t',

    # editing
    '<ctrl-f>': 'fake-key <Right>',
    '<ctrl-b>': 'fake-key <Left>',
    '<ctrl-a>': 'fake-key <Home>',
    '<ctrl-e>': 'fake-key <End>',
    '<ctrl-n>': 'fake-key <Down>',
    '<ctrl-p>': 'fake-key <Up>',
    # '<alt-f>': 'fake-key <Ctrl-Right>',
    '<alt-b>': 'fake-key <Ctrl-Left>',
    '<ctrl-d>': 'fake-key <Delete>',
    '<alt-d>': 'fake-key <Ctrl-Delete>',
    '<alt-backspace>': 'fake-key <Ctrl-Backspace>',
    '<ctrl-w>': 'fake-key <Ctrl-backspace>',
    '<ctrl-y>': 'insert-text {primary}',

    # Numbers
    # https://github.com/qutebrowser/qutebrowser/issues/4213
    '1': 'fake-key 1',
    '2': 'fake-key 2',
    '3': 'fake-key 3',
    '4': 'fake-key 4',
    '5': 'fake-key 5',
    '6': 'fake-key 6',
    '7': 'fake-key 7',
    '8': 'fake-key 8',
    '9': 'fake-key 9',
    '0': 'fake-key 0',

    # misc
    '<ctrl-c><v>': 'spawn --userscript ~/.bin/open_in_mpv.sh',


    # Help
    '<ctrl-h><b>': 'open qute://bindings',
    '<ctrl-h><h>': 'set-cmd-text -s :help',
    # escape hatch
    '<ctrl-g>': ESC_BIND,
}

c.bindings.commands['command'] = {
    '<ctrl-s>': 'search-next',
    '<ctrl-r>': 'search-prev',

    '<ctrl-p>': 'completion-item-focus prev',
    '<ctrl-n>': 'completion-item-focus next',

    '<alt-p>': 'command-history-prev',
    '<alt-n>': 'command-history-next',

    # escape hatch
    '<ctrl-g>': 'leave-mode',
}

c.bindings.commands['hint'] = {
    # escape hatch
    '<ctrl-g>': 'leave-mode',
}


c.bindings.commands['caret'] = {
    '<ctrl-e>': 'move-to-end-of-line', 
    '<ctrl-a>': 'move-to-start-of-line', 
    '<ctrl-space>': 'selection-drop',
    '<escape>': 'mode-leave',
    '<Return>': 'yank selection', 
    '<Space>': 'selection-toggle',
    '<p>': 'move-to-start-of-prev-block', 
    '<n>': 'move-to-start-of-next-block', 
    
    # config.bind('h', 'move-to-prev-char', mode='caret')
    # config.bind('j', 'move-to-next-line', mode='caret')
    # config.bind('k', 'move-to-prev-line', mode='caret')
    # config.bind('l', 'move-to-next-char', mode='caret')
    '<ctrl-b>': 'move-to-prev-char',
    '<ctrl-n>': 'move-to-next-line',
    '<ctrl-p>': 'move-to-prev-line',
    '<ctrl-f>': 'move-to-next-char',

    # escape hatch
    '<ctrl-g>': 'selection-toggle',
}

c.bindings.commands['insert'] = {
    # editing
    '<ctrl-f>': 'fake-key <Right>',
    '<ctrl-b>': 'fake-key <Left>',
    '<ctrl-a>': 'fake-key <Home>',
    '<ctrl-e>': 'fake-key <End>',
    '<ctrl-n>': 'fake-key <Down>',
    '<ctrl-p>': 'fake-key <Up>',
    '<alt-f>': 'fake-key <Ctrl-Right>',
    '<alt-b>': 'fake-key <Ctrl-Left>',
    '<ctrl-d>': 'fake-key <Delete>',
    '<alt-d>': 'fake-key <Ctrl-Delete>',
    '<alt-backspace>': 'fake-key <Ctrl-Backspace>',
    '<ctrl-w>': 'fake-key <Ctrl-backspace>',
    '<ctrl-y>': 'insert-text {primary}',
    '<ctrl-g>': 'leave-mode'

}
