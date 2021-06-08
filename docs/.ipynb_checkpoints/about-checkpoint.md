## Developer Notes
The lead author built this webbook on a Raspberry Pi 4B (4GB) running Ubuntu 20.XX, an Apache Web Server, a JupyterHub (fully encrypted) with iPython extensions, R core, Latex, and MkDocs with extensions.  The deployment hardware is an Amazon Web Services Virtual Private Server (Lightsail Instance) in the West Virginia Server Farm (typically the container is run on x86-64 Xeon hardware)

Direct editing on the AWS server is possible, but the typesetting may not render correctly; additionally running some of the notebooks will use up the daily allocation of compute time on the server and the whole thing will hang up; remember to do all development and testing on the Raspberry PI or your laptop.  The development server is hardware cloned weekly (it takes 12 hours, during which it is inaccessible) 

A working backup is maintained at [https://github.com/dustykat/p4e](https://github.com/dustykat/p4e).

## P4E
The purpose of the webook/repository is to maintain a convienent back-up of course content for rapid migration across servers.  
The name is forwarded from an earlier work by the lead author by the same title that was specific to Python 2.7 with the intent of building web applications for server-side computation; here it is just short and convienent.

## Special Notes
1. The structure is written to work on a web host, with hostname == `atomickitty.ddns.net`, if you clone to another server you will have the lovely task of changing the links.  The string editor `sed` will become your friend!

2. Materials herein come from many sources. Sources in notebooks are at least cited by a URL.  As the content matures, proper citations are to be inserted.

3. If you install the full website, the `3-Readings` directory contains copyrighted materials and should be exposed with care on a web server; because no-one reads anymore, its probably safe enough to protect using a simple `uid:pwd` approach and changing the credentials from time to time. I use the materials during lectures to point out where I obtain various computational ideas.

## How to Use
1. Clone the entire repository to /var/www/html/p4e.  Have your main index point to this directory i.e. `http://your-fqdn-server.org/p4e/site/`
You can see working example at https://3.137.111.182/p4e/ (You will have to set a browser exception to accept the self-signed certificate)

## Syncronization Notes:
1. Sync with 3.137.111.182/engr-1330-webbook/ (AWS server -- primary and live website copy)
2. Sync with 75.3.84.227:192.168.1.75/ (Raspberry Pi -- developer and backup website copy)
3. Sync with 75.3.84.227:192.168.1.79/ (Macintosh -- developer copy)

# About this document

Put something here about the document, authors, copyright (GPL or MIT Open License)

## On-Line Book Author's Notes

- Inserting Code Fragments

To insert a code fragment such as `print('Hello World')` simply indent in the source file used to generate the document

    print('hello world')
    
These fragments can be cut-and-paste into a JupyterLab notebook.

- Inserting Images

If the image is taken from a URL, use the following:

    ![image-name (a local tag)](url_to_image_source)

Such as:

    ![image-name](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqn40YbupkMAzY63jYtA6auEmjRfCOvCd0FA&usqp=CAU)

Which will render a black swan:

![image-name](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqn40YbupkMAzY63jYtA6auEmjRfCOvCd0FA&usqp=CAU)

If the image is local to the host replace the url with the path to the image.

- Inserting URL links

This is a variation of images, but without the `!`, such as

    [link-name-that-will-display](url_to_link_destimation)
    
For example the code below will link to the black swan search results:

    [link-to-images-of-black-swans](https://www.google.com/search?q=images+of+black+swan&client=safari&rls=en&sxsrf=ALeKk03oIoQ387TWjJoKzX-D_b7o1to43Q:1613002985584&tbm=isch&source=iu&ictx=1&fir=L2P5MiS1ICLTxM%252CC6BDdJoXT9KcEM%252C_&vet=1&usg=AI4_-kTXrBMpj__xL5IkGCshrXTp04fX3w&sa=X&ved=2ahUKEwiCneivyODuAhVJBs0KHY88CaAQ9QF6BAgUEAE&biw=1447&bih=975#imgrc=i_lxoojURNE3XM)

[link-to-images-of-black-swans](https://www.google.com/search?q=images+of+black+swan&client=safari&rls=en&sxsrf=ALeKk03oIoQ387TWjJoKzX-D_b7o1to43Q:1613002985584&tbm=isch&source=iu&ictx=1&fir=L2P5MiS1ICLTxM%252CC6BDdJoXT9KcEM%252C_&vet=1&usg=AI4_-kTXrBMpj__xL5IkGCshrXTp04fX3w&sa=X&ved=2ahUKEwiCneivyODuAhVJBs0KHY88CaAQ9QF6BAgUEAE&biw=1447&bih=975#imgrc=i_lxoojURNE3XM)

