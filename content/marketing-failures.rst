#####################################################
Reflections and lessons from failed React workout app 
#####################################################

:date: 2019-10-25 10:49
:author: marijan
:slug: reflections-and-lessons-from-failed-react-workout-app
:lang: en
:tags: freelancing, skills, frontend, react
:cover: assets/images/header_doggy_teacher.jpg
:status: published

This story is about failed personal project I took between jobs. **How
microscopic end result I have to show. But still got something valuable, or
not, you be the judge.**

  - Update 25 Mar 2020. In the mean time I did "finish" `React Django GraphQL app`_ for
    reporting wild dumps

.. _React Django GraphQL app: https://github.com/msvalina/jun-a-k

Background
====================

It's fall of 2015. Four years ago. I quit my job as Magento backend
developer. It lasted only three months... Preparation for position took
learning PHP for a year, and some months. On mornings before daily
programing job. But that is a different story. So I need a new job, but I
don't have to rush it. I'm thinking to myself. Let's build simple workout app
for exercise routine I'm doing. Let's build it with some new technology that
will help me land a new job.

App and technology
===================

  Workout routine for app is from `StartBodyweight.com`_, it's simple and
  good for beginners starting bodyweight exercises. It's based on this infographic poster.

.. _StartBodyweight.com: http://www.startbodyweight.com/2014/01/basic-routine-infographic-poster.html

.. image:: |static|/assets/images/startbodyweight-com-poster.jpg
    :width: 75%
    :align: center
    :target:  http://www.startbodyweight.com/2014/01/basic-routine-infographic-poster.html
    :alt: Start bodyweight poster


Web is not going anywhere. JavaScript is not going anywhere. I should orient
toward them, is my thought stream. It's new beginning and I'm choosing
to learn new — as some would describe — revolutionary technology. It's
React — A JavaScript library for building user interfaces — invented at
Facebook.

As it is with paradigm shifts, new tech, best practices are not
established for some time after invention. And in React case from start it is 
explicitly minimal in nature. Also, Facebook did not lead the way at the time
with supporting frameworks, tools, and practices.

That left a lot of space for enthusiast developers to fill the gaps needed to
make complete application with React. **Explosion of boilerplates code
happened.** Small frameworks that provide scaffolding code. 

There are many questions in front of me. Can I build something useful only
with React? Which boilerplate to choose? Should I build only client side
application? Why not build backend in JS also? I should go with express,
right? How good is that MongoDB that everyone is talking about? Why not use
JSON Web Token for authentication? Why not use Server Side Rendering to speed
up loading time? What about latest ECMA script standard? Of course I should
use webpack, right? And so on...

These questions lead me to try and experiment with different approaches.
A lot of research, and not so much development.


Result
=======

I spent two and a half months on project. On backend side, we can say that
minimal viable product, working API is done. It support users, authentication,
progressions, progression entries, and workout sessions.

From the design side. What I have to show are this half baked wireframes:

.. image:: |static|/assets/images/sbw-wireframe.jpg
    :width: 95%
    :align: center
    :alt: Start bodyweight app wireframes


And from frontend there is almost nothing. I tried to use, many different boilerplates.
Started with simple.

* react + webpack + babel
* `react + react-router + react-hot-loader`_

Then figured I wanted state management. I tried three different redux
implementations, with all latest bells and whistles.

- `universal-redux-jwt`_
- `react-redux-jwt-auth-example`_
- `react-redux-universal-hot-example`_

So that in the end I would settle on react-redux-universal-hot-example.
And my time expired because I got new job offer. Which I took.

.. _react + react-router + react-hot-loader: https://github.com/kriasoft/react-starter-kit/compare/v0.4.0...v0.4.1
.. _universal-redux-jwt: https://github.com/bdefore/universal-redux-jwt
.. _react-redux-jwt-auth-example: https://github.com/joshgeller/react-redux-jwt-auth-example
.. _react-redux-universal-hot-example: https://github.com/erikras/react-redux-universal-hot-example


Mistakes 
=========

Why did I do so little?

Part of story can be describe as distraction...

.. image:: |static|/assets/images/boilerplate-distracion.jpg
    :width: 80%
    :align: center
    :alt: Distracted boyfriend meme looking at new boilerplate 


Part of the plan was to do everything by myself.

But that is also part of the problem.

I thought I have time. 

I had time, just not as much as I needed.

The ever present problem of estimation in software development...

Trying to use every possible cutting edge technology at the time...


Leesons
========

**New technology and fast results are not good combination.**

It's easy to underestimate complexity of simple applications.

**R&D is not development.**

Minimum viable product. Repeat MVP, MVP, MVP.

On JavaScript fatigue
----------------------

Many before me have identified this phenomenon as `JavaScript fatigue`_. I
would not say this is that big of problem. Yes it would be easier if there
were standards, best practices and less choices.
But bigger problem in my case is that **I was learning too many things at
once.** I'm not seasoned JavaScript developer. That meant, a lot of catching
up, and a lot of unsuccessful pitfall avoidance.

.. _JavaScript fatigue: https://www.quora.com/Why-is-Javascript-Framework-fatigue-considered-a-big-problem


What did I get from all this boilerplates?
-------------------------------------------

Well I did actually bother to understand every boilerplate that I used. I did
my homework on understanding nodejs, express, mongoose, babel, on the backend side.
And on frontend side react, webpack, SSR, babel, redux. My head was not in the sand.



Conclusion 
==========

It's blast from the past. My broken truth with reflections. A way to draw
leassons from failed project. Showcase of my current abilities. Failed
showcase, but still. It should at least shed some light at my skill as
Frontend DevOps Engineer, or as failed Full Stack Developer. Thank you for
reading. Have a nice day. 💗
