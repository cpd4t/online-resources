#!/usr/bin/python
import os
import re
import argparse


def make_html():
    #process with pandoc
    print("making html")
    os.system('pandoc -o {0}.html {0}.md -fmarkdown-implicit_figures'.format(args.name))

#could do just the ones related to the file
def upload_assets():
    #upload assets
    print("uploading...")
    os.system("rsync -avz -e 'ssh' --progress assets/ cpdforteachers@cpdforteachers.com:/var/www/vhosts/cpdforteachers.com/website/public/assets/")

def post_process():

    print("post process")
    # do some search and replace stuff to get the html as we need
    with open("%s.html" % args.name) as fh:
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

        m = re.search('^<p>youtube<a href="([^"]+)">.*</a></p>',line)
        if m:
            out += '<iframe width="420" height="315" src="%s" frameborder="0" allowfullscreen></iframe>' % m.group(1)
            continue

        #otherwise
        out += line

    with open("%s.html" % args.name, 'w') as fh:
        fh.write(out)

def copy_paste():
    #put into clipboard
    os.system('cat %s.html | xclip -selection c' % args.name)
    print("copied html into clipboard")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="process and upload cpd resources")
    parser.add_argument('--name', action='store', 
        help="name of markdown file", required=True)
    parser.add_argument('--upload', action='store_const', const=True,
        help="upload content", default=False)

    args = parser.parse_args()
    
    #process markdown
    make_html()
    #post process html
    post_process()
    #upload assets
    if args.upload:
        upload_assets()
    else:
        print("use --upload to update assets directory on server")
    #copy html into paste buffer
    copy_paste()
