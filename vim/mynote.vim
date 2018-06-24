echo has("python")
w   move to beginning of next word

b   move to previous beginning of word
e   move to end of word
ge  move to the end of previous word
W   move to beginning of next word after a whitespace
B   move to beginning of previous word before a whitespace
e   move to end of word before a whitespace
f
F
t
T
d0 delete until the cursor
d$ delete after the cursor

###############################
0   move to beginning of line
$   move to end of line  
_   move to first non-blank character of the line 
g_  move to last non-blank character of the line            

H   move to top of screen
M   move to middle of screen
L   move to bottom of screen

zz  scroll the line with the cursor to the center of the screen
zt  scroll the line with the cursor to the top
zb  scroll the line with the cursor to the bottom
Ctrl-D  move half-page down
Ctrl-U  move half-page up
Ctrl-B  page up
Ctrl-F  page down

:ju
Ctrl-i  jump to next cursor position (after Ctrl-O)
ctrl-o
Ctrl-Y  move view pane up
Ctrl-E  move view pane down

n   next matching search pattern
N   previous matching search pattern

*   next whole word under cursor
#   previous whole word under cursor
g*  next matching search (not whole word) pattern under cursor
g#  previous matching search (not whole word) pattern under cursor

%   jump to matching bracket { } [ ] ( )
fX  to next 'X' after cursor, in the same line (X is any character)
FX  to previous 'X' before cursor (f and F put the cursor on X)
tX  til next 'X' (similar to above, but cursor is before X)
TX  til previous 'X'
;   repeat above, in same direction
,   repeat above, in reverse direction
#########################
help key
g command
g; go to place of last change
g, go to place of last change

gm go to middel 
gv reselect

ftplugin  filetype plugin

:runtime! ftplugin/man.vim
vimtutor
Much like the relationship between
" reverse line order
" The "^" regular expression matches the beginning of the line (even if the line is blank). The :move command moves the matching line to after the mythical zeroth line, so the current matching line becomes the first line of the file. As the :global command is not confused by the changing line numbering, :global proceeds to match all remaining lines of the file and puts each as the first.

:g/^/m 0

" This also works on a range of lines. First move to above the first line and mark it with "mt". Then move the cursor to the last line in the range and type:
:'t+1,.g/^/m 't
 g Ctrl-G " count word
gUw ( motion )
guw
g~
:help function-list

:set            - shows vars different from defaults
:set all        - shows all values
:set foo?       - shows the value of foo
:set foo+=opt   - add opt to the value w/o changing others
:set foo-=opt   - remove opt from value
:set foo&       - reset foo to default value
:setlocal foo   - only the current buffer
:let &foo = 1

zf3j " folding
zo - open
zc - close

g?	ROT13 encoding
>	shift right
<	shift left
  
map <C-L> :noh<CR>:redraw!<CR>

" The first one below, when typing in insert mode, changes every occurence of ;so to System.out.println(); and leaves you in insert mode between the parentheses!
 imap ;so System.out.println();<left><left>

" while in insert mode, moves you to the end of the next line when you type ;ne
 imap ;ne <esc>/;<cr>a

" The last one puts bold html tags around something you "have" visually :jselected.
" <B> is normal word
" <c-r>z will paste from z register


" The following one puts</B> bold html tags around something you have visually selected.

 vmap <buffer> ;bo "zdi<B><c-r>z</B><esc>

Normally a CTRL-Y in Insert mode does a "vertical copy." That is, it copies the character in the same column from the line immediately above the cursor. For example, a CTRL-Y in the following situation would insert an "m" at the cursor:

 <c-y> in Insert mode does vertical copy

"  escaped is required in exe
 :exe "normal! mqA;\<esc>'q"

 mq will mark, 'q return \<esc>

" This will search for the keywords "if", "else", and "endif"
"under or after the cursor.  Because of the 'p' flag, it
" returns 1, 2, or 3 depending on which keyword is found, or 0
:echo search('\<if\|\(else\)\|\(endif\)', 'ncpe')

" buffers command
:ls
:b <number>
:b <tab completion>
:bd
:bd!

Ctrl-W in normal mode:
:h ^w

Ctrl-W in insert mode:
:h i^w

Ctrl-W in visual mode:
:h v^w

Ctrl-W in command mode:
:h c^w
Open help in another tabpage:

:tab h ^w

	You can try out the examples by yanking the lines from the text here
	and executing themhe examples by yanking the lines from the text here
copy the selected area
:normal '<y'>
:normal `<y`>

" ? means ignore case
" # means case sensitive
if v:progname =~? "evim"

 
      \ if line("'\"") >= 1 && line("'\"") <= line("$") && &ft !~# 'commit'

"  in command line usr <c-r>" to paste from register
"  using <c-v> 
"
FORCING A MOTION TO BE LINEWISE, CHARACTERWISE OR BLOCKWISE

When a motion is not of the type you would like to use, you can force another
type by using "v", "V" or CTRL-V just after the operator.
Example: >
	dj
deletes two lines >
	dvj
deletes from the cursor position until the character below the cursor >
	d<C-V>j
deletes the character under the cursor and the character below the cursor. >

	foo\(bar\)\@=		"foo" in "foobar"

	foo\(bar\)\@!		any "foo" not followed by "bar"

	\(an\_s\+\)\@<=file	"file" after "an" and white space or an

  this is equivalent to \zs

	\(foo\)\@<!bar		any "bar" that's not in "foobar"

"g command"
z command

<c-v>
<c-r>
<c-w>

normal! command
" eval
exec normal!

vert

sba;
ba
tab ba
let @q="2dw"
then run normal @q
register with a macro that deletes two words

ga
display hex and ASCII value of character under cursor
g8
of utf-8 character under cursor
面值英镑的
viw
yiw

count the number of occurrences of "forward" in a file
:%s/forward//gn

ci"
change all the words in between two quotes

foo\(bar\)\@!		any "foo" not followed by "bar"
/foo\(bar\)\@= foo followd by bar
 
	a.\{-}p\@!		"a", "a p", "app", "appp", etc. not immediatea
	a.p\@!		"a", "a p", "app", "appp", etc. not immediatea

	if \(\(then\)\@!.\)*$	"if " not followed by "then"

	\(foo\)\@<!bar		any "bar" that's not in "foobar"

	foo\(bar\)\@=		"foo" in "foobar"
  this is equivalent to \ze
  
  in python ?=/?!/?<=/?<!
        \b \b \A \Z

help ins-competion
help regex
set cmdheight=2
\v(\zs(\w+)\ze\s){4}
help ^a ( increase number )
help ctrl-a
gcc
help v_b_a
help i_ctrl-r
g ctrl-a
g ctrl-g
cq quit without writing
gf open the file whose name is under the cursor
# moving around
w 
e
ge
b
# g command
g/foo/z#5 | echo '======' #z#5 5 lines
:.,$g/^\d/exe "normal! \<C-A>" # increemnt each number at the start of a line
:g/^/m0 # reverse a file
:2,8co15 #copyy line 2 through 8 after line 15
1
:4,15t$ #copy lines 4 through 15 to end of file
:-t$ # copy previus line to end of file
:-t+ #copy prvisous line to next line
1
:m0 #move current line to top of file
:.,+3sm$-1 # next to last line
g!/foo/d
g/^\s*$/d
g/^/pu = \"\n\"
g/foo/pu _
g/foo/t$
g/foo/m$ (0)
qaq:g/foo/y A
g/^/m0 # reverse the file
g/foo/d_ ( _ fast deleting without putting things into register )
#to collapse empy lines inclding withspace
%s/^\_s\+/\r/g
#\_s match space and tab and end of line. \r insserts carriage return specific to file format

#compress multiple occurrences of blank lines into a single blank line
:v/./,/./-j
2,4 join # join 2 to 4 line
:lcd %p:h (each window have a local crrrent directory, % gives the name of the current file, %:p gives its full path and %:p:h gives its directory)
:cd %p:h
:g/pattern/normal @q
:g/^\(.*\)\(\r\?\n\1\)\+$/d :%uniq

#to count the number of matches of pattern, use the substitute command wiht n flage
%s/foo//gn
#to count the number of occurrence of last used search pattern
nnormap * *<c-o>:%s///gn<CR>
<c-o> here returs the cursor to where it started
%s///gn
#To move the cursor to the matched string while typing the search pattern
set incsearch 
#press / then ctrl-r ctrl-w ( ctrl-a ) to copy the current word to the commnad line (ctrl-r [register])
#after searching an empty search pattern will represent the last search and it work with /,:s,:g
3/foo will serarch the third occurrence of foo

#z command
zz
zb
z<CR>


when defining nnoremap, you can use :call or :exe
in script, you call call exe "normal ..."
search() is function but s/foo/bar/ is ex command
foo\_A*bar
\_[aeiou]+ 
:set ft=sql
we can explore the completion feature to get all the system variable
syntax file and color file are in $VIM
echo <c-d> # list all the function
echo $<tab> # list all the variable
in command line, 
<c-b>
<c-e>
<c-w>
<c-h>
<c-p>

for commandline ( ipython and bash )
<c-a>
<c-e>
<c-f>
<c-b>

<c-d>
<c-h>
<c-w>
<c-u>
<c-k>

<c-y>
<c-xx>
<c-p>
<c-r>
/\v%>2l%<10lfoo
:help :z
:help search-range
let i=1 | g/^/s//\=i/|let i=i+1

string = "{:{fill}{assign}{width}}"
string.format("hello",fill="x",assign=">",width = 10)
gi
4gI

s = "one two 3.4 5,6 seven.eight nine,ten"
spliter = r'\s|[,.]'
(?<!\d)
(?<=\d) # this is as as \zs
(?=\d) # this is as good as \ze
(?!\d)
> parts = re.split('\s|(?<!\d)[,.](?!\d)', s)
['one', 'two', '3.4', '5,6', 'seven', 'eight', 'nine', 'ten']
In other words, you always split by \s (whitespace), and only split by commas and periods if they are not followed (?!\d) or preceded (?<!\d) by a digit."

(gao)@<!yan(lijia)@!

===============for git ========

Check $ git log, then copy SHA id of 2 different commits and then run git diff command with those ids, for example:

$ git diff (sha-id-one) (sha-id-two)

g/foo/v/bar/ #same line
g/foo/g/bar/
g/foo//bar/ #different line

/foo/,/bar/g/foo/s/foo/bar/
or 
g/foo/,/bar/-j # - means leving one line from last line
to represent emply line
1) /^$/
2)/\n/
to represent non-emply line
1) /./

s/\v([.])@<!<./\u&/

\v([.])@<!<. # can find the first alpha not following '.'
help spell
@: to repeat the last command

      \c \v
:nnormap <tab>
nnormap <leader>t
nnormap <Space>t
help < <tab>
help i <tab>
cs"'
ds"
ysiw""
yssb
csurround
#####
Setup remote repository:

ssh git@example.com
mkdir my_project.git
cd my_project.git
git init --bare
###
On local machine:

cd my_project
git init
git add *
git commit -m "Initial commit"
git remote add origin example.com:my_project.git
git push -u origin master
########

git remote add pb git@github.com:gaoyan0629/dmv1.git
## this means we can add a point to remote address, later we can do a fetch

git push -d origin feature_x
" remove the branch from remote
" push will push both master and branch
git diff --staged
git diff
git log
" Unstaging a Staged File
git reset HEAD CONTRIBUTING.md
