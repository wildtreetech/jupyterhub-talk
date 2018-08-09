class: middle, center, title-slide

# Binder


.footnote[Tim Head, Wild Tree Tech, JupyterCon 2018]

---

# Demo

Because why not?

---

# Libraries

.center.width-60[![](img/Library_of_Ashurbanipal_The_Flood_Tablet.jpg)]

.footnote[By <a href="//commons.wikimedia.org/wiki/User_talk:F%C3%A6" title="User talk:Fæ">Fæ</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=10939144">Link</a>]

???

Earliest libraries were archives of clay tablets. Appeared in Mesopotamia about 2600BC. Making clay tablets was hard work, as you could imagine. Sharing and recording information is something humans have been doing for a very long time.

---

# Libraries

https://unsplash.com/photos/gFrhMONDf9o

???

Things have changed a bit since then. We invented paper and the printing press. Spreading information via books and documents has become easy! We can do this at scale!

---

# Libraries

https://unsplash.com/photos/PkbZahEG2Ng
https://unsplash.com/photos/ljp-ewA23lc

???

Modern libraries are modern!

---

# Information is now digital

<!--
<img src="img/British_Museum_Reading_Room_Panorama_Feb_2006.jpg"
  style="width: 120%; margin-left: -10%;" />

.footnote[By <a href="//commons.wikimedia.org/wiki/User:Diliff" title="User:Diliff">Diliff</a> - <span class="int-own-work" lang="en">Own work</span>, <a href="https://creativecommons.org/licenses/by/2.5" title="Creative Commons Attribution 2.5">CC BY 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=564849">Link</a>] -->

.larger[An article about computational science in a scientific publication is not the scholarship itself, it is merely advertising of the scholarship. The actual scholarship is the complete software development environment and the complete set of instructions which generated the figures.]

-- _Buckheit and Donoho
(paraphrasing John Claerbout),
WaveLab and Reproducible Research, 1995_

???
Needs a picture. Illustrate point that information is now in computers and code, not paper or PDF anymore.

---

class: middle, center

# Today: Getting other people's code to run

---

# Other people's code is ... fun?!

.center.width-70[![](img/python_environment_2x.png)]

.footnote[From https://xkcd.com/1987/]

---

# The Wild West Model

Anything goes, all the modern tools, all the time.

You have discussions like:

**A:** I tried to run your script to generate the charts of our monthly sales numbers. It complains about not finding the Shedazzle shell??

**B:** Ah yeah, Shedazzle is the latest in AI powered shell, everyone is using it now, you should also change. bash really hurts your productivity.

**A:** Ah ok, so ... uhm I guess I'll try installing Shedazzle then ...

**B:** Make sure to install the latest beta, current release is a bit flakey.

---

# The Corporate IT Lockdown Model

Your IT department tightly controls what can be installed, there are
approved tools that you shall use.

**A:** Could we upgrade our scikit-learn version? They fixed several bugs that we have been working around for the last 6 months.

**B:** Any new versions need to be audited first. Let me CC **C** from audits.

**C:** Correct, all new code needs to be audited. We have a monthly meeting to prioritise the audit backlog.

**D:** The Audit department needs a bigger headcount if we are meant to do more audits.

**A:** Ok, well, I guess we keep working around the issues then ...

---

# What do we need for practical code sharing?

* The computational tools to solve a problem
* A way to pack it all so others can use it
* A way to communicate and share our work
* A way to do all of this relatively easily and accessibly

---

# Open-source languages

.gallery[
![](img/Python-logo-notext.svg)
![](img/Rlogo.svg)

![](img/julia-logo.svg)
![](img/cpp_logo.svg)
]

---

# Web native editors

.gallery[
![](img/jupyter-logo.svg)

![](img/rstudio-logo.png)
]

... and many more.

---

# Sharing your work

.gallery[
![](img/github-logo.svg)
![](img/gitlab-logo.svg)

![](img/bitbucket-logo.png)
]

---

# Specifying dependencies

.center.width-20[![](img/docker-logo.png)]

But my language has a package manager!

* language specific tools work well if you only use one language
* some tools are easier to install via the operating system's package manager
* real world projects use several languages

To specify the complete computational environment a container is the right
level of abstraction.

---

# Easy?

.larger[All the technical pieces exist but they require significant expertise to operate
and combine.]

--

.center.width-60[![](img/Library_of_Ashurbanipal_The_Flood_Tablet.jpg)]

---

# Just use our framework!

.center.width-100[![](img/jakob-owens-373320-unsplash.jpg)]

---

class: middle, center

# repo2docker

---

# Creating Containers

Writing a `Dockerfile` is hard, and tedious. Not my definition of fun.

Most programming languages already have a way to specify dependencies.

Can't we automate creating a Docker image?

---

# repo2docker builds and runs containers from a directory

.center.width-100[![](img/repo2docker-docs2.png)]

---

# repo2docker understands you

It can parse many different files that specify what dependencies to install.
This means that you can keep working the way you have always been working,
and benefit from `repo2docker` from day one.

Supported configuration files:
* `requirements.txt`
* `environment.yml`
* `apt.txt`
* `REQUIRE`
* `install.R`
* `runtime.txt`
* `postBuild`
* `Dockerfile`

---

.center.width-100.border[![](img/pytudes-demo.gif)]

---

# Back to sharing

```
Hi Tim,

thanks for helping out on our project. To run things
you need to install Docker and then

`pip install repo2docker`.

You need to run it with the URL of the GitHub repo
and it will automatically build a docker image for
you, then launch it. It produces a lot of output but
at the end there is a URL that you need to paste into
your browser. It will show a Jupyter notebook.

Let me know how it goes,
```

.larger[
Can we make it even easier?

Maybe just a link people can click?
]

---

class: middle, center

# Of course!

<a href="https://mybinder.org/v2/gh/norvig/pytudes/master" class="center width-50"><img src="https://mybinder.org/badge.svg" alt="Binder"></a>

---

class: middle, center

# Binding it all together

---

# We have all the pieces

.center[

.width-20[![](img/jupyterhub-logo.png)]

.larger[+

repo2docker

+]

.width-40[![](img/kubernetes-logo.svg)]
]

<a class="github-fork-ribbon" href="https://conferences.oreilly.com/jupyter/jup-ny/public/schedule/detail/71218" data-ribbon="Min's talk (2.40pm)" title="Min's talk (2.40pm)">Min's talk (2.40pm)</a>

---

# JupyterHub with ondemand containers: BinderHub!

.center.width-100[![](img/mybinder-org.png)]


???

Combine `repo2docker` with JupyterHub to build images for any git repository
ondemand.

We call it BinderHub.


---

# https://mybinder.org

A public BinderHub operated by the Binder team.

.center.width-100[![](img/mybinder-org.png)]

<a class="github-fork-ribbon" href="https://conferences.oreilly.com/jupyter/jup-ny/public/schedule/detail/68437" data-ribbon="Yuvi's talk (now)" title="Yuvi's talk">Yuvi's talk (now)</a>

---

# Not just Jupyter Frontends

https://github.com/binder-examples/r

.center.border.width-100[![](img/rstudio-demo.gif)]

---

# Who is building this?

* shout out to all the contributors!
  * super hard to find a picture or a list because we are spread over several repositories
* Join us at https://github.com/jupyterhub/binder
* Chat with us https://gitter.im/jupyterhub/binder
* Become part of the community:
    * use binder and the tools around it,
    * help explain binder to people,
    * follow our tutorials (and then help us improve them)
    * help maintaining the code,
    * take part in the operations,
    * create your own with the zero2binder guide!

---

# Around the world in 80 days

[Users from all around the globe](https://analytics.google.com/analytics/web/#/report/visitors-geo/a101904940w149250546p154152886)

.center.width-100.border[![](img/binder-map-of-users.png)]

---

# What about libraries?

Libraries have always been about curating and spreading knowledge!

First they collected clay tablets, then books, then they managed access to PDFs, next ...

--
.larger[
...a BinderHub in every library.
]
---

# BinderHub is a step forward in making computational work easier to reproduce

Combines the stability and scalability of JupyterHub with ondemand image building.

Anyone who wants can now make their computational project "one click" reproducible: [![Binder](http://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/AllenDowney/ThinkDSP/master?filepath=code/cacophony.ipynb)

Based on state of the art cloud orchestration tools.

Can be deployed by anyone: https://binderhub.readthedocs.io/en/latest/

---

class: middle, center

# Encore

now we start the exciting part

---

# Challenge

Can you (this room) move the needle on the number of live binders?

.larger[
Visit http://bit.ly/2t9Bjql to launch your first binder.
]

<iframe src="https://grafana.mybinder.org/d-solo/fZWsQmnmz/pod-activity?refresh=30s&orgId=1&panelId=3" width="100%" height="300" frameborder="0"></iframe>

---

# Interactive documentation

https://spacy.io/usage/linguistic-features#pos-tagging

.center.width-50[![](img/juniper.png)]

---

# GUI like things

* https://github.com/binder-examples/appmode
* https://github.com/SimonBiggs/scriptedforms/blob/master/README.md

---

# Real GUIs - X servers!

* https://mybinder.org/v2/gh/betatim/nbnovnc/add-xeyes

.center.width-100.border[![](img/xeyes-demo.gif)]


---

# Wild Tree Tech

.center.width-10[![](assets/logo_wtt.png)]

Tim is a doctor of experimental physics, worked at CERN and EPFL,
contributor to the PyData ecosystem.

Wild Tree Tech builds bespoke solutions for clients all around the world,
from startups to UN organisations.

* digital products that leverage machine-learning and AI,
* small and large JupyterHub deployments.

Visit [http://www.wildtreetech.com](www.wildtreetech.com).

---

class: bottom, center

# Fin.
