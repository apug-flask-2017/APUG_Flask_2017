Visible Flask – Introduction


This is not a tutorial.  I list multiple tutorials with different styles of development, different package support, and different scope in the Resources section below.

My experience with the tutorials was that I did not get any real understanding of “how” Flask worked – or even what it was worth to me – during the course of following the tutorial.  Also, I had trouble evaluating the approaches of the different tutorials to determine which would work best for me.  No complaints.  The authors were doing their best to disclose their experience and guide me to a point where I could exploit Flask effectively.  But, because of my own learning patterns, I was frequently frustrated – and frequently lost – as I worked my way through the examples.

Most problems stem from our ignorance of the details Flask smooths over for us.  We do not understand enough about the HTTP transaction protocols and pitfalls.  We do not understand the history of Apache’s mod_python or WSGI.  We want to master a full, secure, multi-threaded web application with an Nginx webserver and Postgres database backend.  Maybe we’ll get there by the end of this series.

Definition: EXPERT – someone who has done it more times than you have.  Usually that means once.

I have done all of this stuff at least once.  Maybe I have done some of them more times than you have.

If you don’t “get” what I just showed you, ask me to do it AGAIN – or ASK ME TO DO IT A DIFFERENT WAY.  (Limit: two, maybe three, ways.) 

BACKTRACKING is OK.  Ask me to go back a few steps to a previous example.

Maybe not “Best Practices.”  But “Good” or at least “Workable” practices + some deeper understanding that will help you to find “Better Practices.”

Yak Shaving:  You want to do A.  But in order to do A, you have to learn B.  But you cannot learn B without understanding C.  And you cannot do C until you have installed D.  And D depends on E.  And before you can get E, you have to know …  Yak Shaving.

The exercise we are about to undertake is not Yak Shaving, though it will sometimes have that feel.  Most of what we will see and do can be presented in a tutorial without any real explanation – monkey see, monkey do style.


 ![Image of Visible Man]
(/blob/master/VisibleMan.jpg)



Examine the guts of Flask – from skin to skeleton.

Includes the subsystems or companion packages on which developers often rely.
