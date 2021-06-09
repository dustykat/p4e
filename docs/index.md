# <p style="text-align:center">Python (and Data Science) for Engineers: <br> A WebBook to Accompany <br> "ENGR-1330 Computational Thinking and Data Science" <br> at Texas Tech University </p>

<p style="text-align:center">by <br><br>Theodore G. Cleveland and Farhang Forghanparast<br></p>

<p style="text-align:center">with contributions from :<br> Dinesh Sundaravadivelu Devarajan, Turgut Batuhan Baturalp (Batu), Tanja Karp, Long Nguyen, and  Mona Rizvi </p>

Copyright © 2021 Cleveland and others, *The contents of this book are licensed for free consumption under the following license: [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/)*

## Introduction
 
This on-line webbook is a collection of iPython/JupyterLab articles (as in the article class in LaTex) useful for ENGR-1330 sections taught by the first two authors; It is organized in a topical sequence envisioned by the lead author -- instructors are not expected to use all the articles, but instead would select appropriate articles as readings to support their course.  A couple of suggested syllabi are included in the [Appendix](https://#).

suggested citation: 

<font color=magenta>Theodore G. Cleveland, Farhang Forghanparast, Dinesh Sundaravadivelu Devarajan, Turgut Batuhan Baturalp (Batu), Tanja Karp, Long Nguyen, and Mona Rizvi. (2021) * Python (and Data Science) for Engineers: A WebBook to Accompany ENGR 1330 at TTU *, Whitacre College of Engineering, DOI (pending) [https://3.137.111.182/p4e/](https://3.137.111.182/p4e/)</font>

## Document History
This document is a living document and is updated frequently, Python is an ever evolving tool and stuff that works today will be constructively broken by the development team (python.org) in their quest for continuous improvement.  Generally these changes occur in the packages (libraries, external modules) and base python is quite stable.  The scripts herein are intended for use with Python 3.X installations, and may not be backward compatable.

## Author/Developer Notes

### Hardware Requirements
The lead author built this webbook on a Raspberry Pi 4B (4GB) running Ubuntu 20.XX, an Apache Web Server, a JupyterHub (fully encrypted) with iPython extensions, R core, Latex, and MkDocs with extensions.  The deployment hardware is an Amazon Web Services Virtual Private Server (Lightsail Instance) in the West Virginia Server Farm (typically the container is run on x86-64 Xeon hardware).

Direct editing and build on the AWS server is possible, but the typesetting may not render correctly; additionally running some of the notebooks will use up the daily allocation of compute time on the server and the whole thing will simply stall for awhile; Its better to do all the development and testing on the Raspberry PI or a laptop, then push changes to the AWS deployment.  

The Raspberry Pi 4B development server's entire filesystem is cloned weekly (roughly 1/2 TB; it takes 12 hours, during which it is inaccessible) 

A current working backup is maintained at [https://github.com/dustykat/p4e](https://github.com/dustykat/p4e).

### GitHub P4E repository
The purpose of the repository is to maintain a convienent back-up of course content and for simple deployment.
The typical method used is to:

1. Develop a chapter on the Raspberry Pi 4B.  When you are happy with the added content, then 
2. Build the book e.g. `sensei@atomickitty:~/p4e$ mkdocs build`  wait until completed; observe warnings, fix any errors, then 
3. Update the repository e.g. `sensei@atomickitty:~/p4e$ git add . && git commit -m "add introduction" && git push`, when prompted for the SSH passphrase, supply it.  This action pushes changes to GitHub and updates the repository.
4. Login to the AWS instance, and navigate to the host location where you store the deployment version and pull the changes e.g. `sensei@ip-172-26-4-2:~/p4e$ git pull` (notice the subtle prompt change, we are on a different machine)
5. Deal with any errors - the pull is a fast forward merge, and sometimes fails, errors are usually fixable easily. 

#### Special Notes
1. The structure is written to work on a web host, with hostname == `atomickitty.ddns.net::3.137.111.182`, if you clone to another server you will have the lovely task of changing the links.  The string editor `sed` will become your friend!  Most of the internal links use the IP address, although some use the DNS entry - this is a result of when the particular content was created; I have tried recently to stick with the IP notation, as i think it is easier to edit using `sed` when the content needs to move to a different host.

2. Materials herein come from many sources. Sources in notebooks are at least cited by a URL.  As the content matures, proper citations are to be inserted.

#### How to Use
1. Clone the entire repository to /var/www/html/p4e.  Have your main index point to this directory i.e. `http://your-fqdn-server.org/p4e/site/`
You can see working example at https://3.137.111.182/p4e/ (You will have to set a browser exception to accept the self-signed certificate)

#### Syncronization Notes:
1. Sync with 3.137.111.182/p4e/ (AWS server -- primary and live website copy)
2. Sync with 75.3.84.227::192.168.1.75/ (Raspberry Pi -- developer and backup website copy)
3. Sync with 75.3.84.227::192.168.1.79/ (Macintosh -- developer copy)

### On-Line Book Author's Notes (How to ....)

All the pages are written in a JupyterLab notebook, then rendered as a markdown file.  The website builder reads the markdown file(s) as directed by the `mkdocs.yml` to build the pages you see on the browser.  It sounds elaborate, but is quite straightforward after some work with the system.

- Inserting Code Fragments

To insert a code fragment such as `print('Hello World')` simply indent in the source file used to generate the document

    print('hello world')
    
These fragments can be cut-and-paste into a JupyterLab notebook.  The source JupyterLab notebook when rendered as markdown, does the indentation automatically.

- Inserting Images

If the image is taken from a URL, use the following in a Markdown cell:

    ![image-name](url_to_image_source)
    
The image will be displayed the `[image-name]` tag can be empty.

Such as:

    ![image-name](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqn40YbupkMAzY63jYtA6auEmjRfCOvCd0FA&usqp=CAU)

Which will render a black swan:

![image-name](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqn40YbupkMAzY63jYtA6auEmjRfCOvCd0FA&usqp=CAU)

If the image is local to the host replace the url with the path to the image; if you anticipate the path on the deployment server, then the image can be used as an html link.

- Inserting URL links

This is a variation of images, but without the `!`, such as

    [link-name-that-will-display](url_to_link_destimation)
    
For example the code below will link to the black swan search results:

    [link-to-images-of-black-swans](https://www.google.com/search?q=images+of+black+swan&client=safari&rls=en&sxsrf=ALeKk03oIoQ387TWjJoKzX-D_b7o1to43Q:1613002985584&tbm=isch&source=iu&ictx=1&fir=L2P5MiS1ICLTxM%252CC6BDdJoXT9KcEM%252C_&vet=1&usg=AI4_-kTXrBMpj__xL5IkGCshrXTp04fX3w&sa=X&ved=2ahUKEwiCneivyODuAhVJBs0KHY88CaAQ9QF6BAgUEAE&biw=1447&bih=975#imgrc=i_lxoojURNE3XM)

[link-to-images-of-black-swans](https://www.google.com/search?q=images+of+black+swan&client=safari&rls=en&sxsrf=ALeKk03oIoQ387TWjJoKzX-D_b7o1to43Q:1613002985584&tbm=isch&source=iu&ictx=1&fir=L2P5MiS1ICLTxM%252CC6BDdJoXT9KcEM%252C_&vet=1&usg=AI4_-kTXrBMpj__xL5IkGCshrXTp04fX3w&sa=X&ved=2ahUKEwiCneivyODuAhVJBs0KHY88CaAQ9QF6BAgUEAE&biw=1447&bih=975#imgrc=i_lxoojURNE3XM)

- Typesetting mathematics

In a markdown cell use dollar signs to delimit mathematics.  A leading and trailing pair (4 characters) centers the results.  In-line leading and trailing (2 characters) left justifies the result  For example, the latex gibberish F(x)=\int^{\tau}_{-\infy}{f(\tau)d\tau} when surrounded by "$" symbol renders:

$F(x)=\int^{\tau}_{-\infy}{f(\tau)d\tau}$


