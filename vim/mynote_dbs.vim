:vert belowright sb N
:vert sb N 
:tab sb N
Chain two commands: tabnew to open a new tab and b <buffer_number> to load the desired buffer in the tab.

:tabnew | b 2

vim -o *.vim 
:tab all

:set nomore
:redir > c.txt
:changes
:redir END
:set more

:%s/.*\zsfoo/bar/
On each line, replace the last occurrence of "foo" with "bar".

:%s/\<foo\>//g
On each line, delete all occurrences of the whole word "foo".
:%s/\<foo\>.*//
On each line, delete the whole word "foo" and all following text (to end of line).
:%s/\<foo\>.\{5}//
On each line, delete the first occurrence of the whole word "foo" and the following five characters.
:%s/\<foo\>\zs.*//
On each line, delete all text following the whole word "foo" (to end of line).
:%s/.*\<foo\>//
On each line, delete the whole word "foo" and all preceding text (from beginning of line).

:%s/.*\ze\<foo\>//
On each line, delete all the text preceding the whole word "foo" (from beginning of line).

:%s/.*\(\<foo\>\).*/\1/
On each line, delete all the text preceding and following the whole word "foo".

:%s/\<foo\(bar\)\@!/toto/g
On each line, replace each occurrence of "foo" (which starts a word and is not followed by "bar") by "toto".

:s/^\(\w\)/\u\1/

If the first character at the beginning of the current line only is lowercase, switch it to uppercase using \u (see switching case of characters).

:%s/\(.*\n\)\{5\}/&\r/

Insert a blank line every 5 lines.
The pattern searches for \(.*\n\) (any line including its line ending) repeated five times (\{5\}).
The replacement is & (the text that was found), followed by \r (newline).
/\%>'a\%<'bfoo
b
 cmap  /\%>'a\%<'bfoo 
 :g/.\n\n\@!/norm o
 :%s/\n\@<!\n\n\@!/\r\r/g
 :g/^$/d
:v/./d
:v/\S/,/\S/-j

let i=1 | 'a,'b g/^/ s//\=i . ":"/ | let i+=1

set guifont=*

set guifont=Consolas:h24

re.sub(r'(?is)(?#heloo)(?P<gao>^a\d{3,}?)(\d{2,}.*\
    ...: z)',r'\g<gao>abc\2abc',string)

set -o emacs
set -o
set +o vi
intrinsic operators of Python
>>> s = 'cat'      # s is an ITERABLE
                   # s is a str object that is immutable
                   # s has no state
                   # s has a __getitem__() method 

>>> t = iter(s)    # t is an ITERATOR
                   # t has state (it starts by pointing at the "c"
                   # t has a next() method and an __iter__() method

junkie
In [8]: mask = m['Name'] == 'Other'

In [9]: m.loc[mask, 'Name'] = ''
#this is pretty underhand
this is going to be breeze

%s/\v(\zs[^\|]*\ze\|){10}/abcde/

