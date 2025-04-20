set nocompatible " 禁用 vi 模式

function! DisplayCenteredHello() abort
    " 创建临时 buffer
    enew
    setlocal bufhidden=wipe  " 关闭时自动删除 buffer
    setlocal buftype=nofile  " 不关联文件
    setlocal nobuflisted     " 不在 buffer 列表显示
    setlocal noswapfile      " 不生成交换文件
    setlocal nonumber        " 不显示行号
    setlocal nowrap          " 不自动换行
    setlocal laststatus=0    " 关闭statusline

    " 获取窗口尺寸
    let win_width = winwidth(0)
    let win_height = winheight(0)

    " 定义要输出的内容
    let lines = [
                \ '  _   _      _ _        __        __         _     _ ',
                \ ' | | | | ___| | | ___   \ \      / /__  _ __| | __| |',
                \ ' | |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| "__| |/ _` |',
                \ ' |  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |',
                \ ' |_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_|'
                \]
    " 计算垂直居中
    let total_lines = len(lines)
    let vertical_padding = max([(win_height - total_lines) / 2, 0])

    " 生成最终内容
    let content = []
    " 添加顶部空行
    call extend(content, repeat([''], vertical_padding))

    " 添加居中内容
    for line in lines
        " 计算水平居中空格
        let padding = repeat(' ', max([(win_width - strdisplaywidth(line)) / 2, 0]))
        call add(content, padding . line)
    endfor

    " 添加底部空行
    call extend(content, repeat([''], vertical_padding))
    " 写入内容
    call setline(1, content)

    " 禁止修改内容
    setlocal nomodifiable

    " 设置键盘映射 (按 q 关闭 Vim)
    nnoremap <buffer><silent> q :qa!<CR>
    echo "Press 'q' to close Vim"
endfunction

" 创建命令调用
command! HelloWorld call DisplayCenteredHello()

" 自动显示
autocmd VimEnter * HelloWorld
