#!/usr/bin/python
import os
import re

name = 'soundbox'

#process with pandoc
os.system('pandoc -o {0}.html {0}.md -fmarkdown-implicit_figures'.format(name))


#upload assets
#scp assets/images/soundbox/* cpdforteachers@cpdforteachers.com:/var/www/vhosts/cpdforteachers.com/website/public/assets/images/soundbox/

with open("%s.html" % name) as fh:
    html = fh.readlines()

out = ''
for line in html:
    m = re.search('^<p>button(<a )(href="[^"]+">.*</a>)</p>',line)
    if m:
        button_class = 'btn btn-primary'
        out += '<p>' + m.group(1) + "class='%s' " % button_class + m.group(2) + '</p>'
        continue

    m = re.search('^<p>scratch<a href="([^"]+)">.*</a></p>',line)
    if m:
        out += '<iframe allowtransparency="true" width="485" height="402" src="http://scratch.mit.edu/projects/embed/%s/?autostart=false" frameborder="0" allowfullscreen></iframe>' % m.group(1)
        continue

    #otherwise
    out += line

with open("%s.html" % name, 'w') as fh:
    fh.write(out)
#put into clipboard
os.system('cat %s.html | xclip -selection c' % name)
