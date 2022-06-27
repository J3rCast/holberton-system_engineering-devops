<div class="project row">

  <div class="panel-body">
    <h2>Background Context</h2>
<p>For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.</p>
<p>Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the <code>//</code>:</p>
<pre class="language-text">sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
</pre>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a href="file:///\\wsl$\Ubuntu\home\jerson\Holberton\rltoken\SJ2eQ7V2iQlCgLc-L96zWg" title="Regular expressions - basics" target="_blank">Regular expressions - basics</a> </li>
<li><a href="file:///\\wsl$\Ubuntu\home\jerson\Holberton\rltoken\qyjWL-J1_qUaZGR690gH1Q" title="Regular expressions - advanced" target="_blank">Regular expressions - advanced</a> </li>
<li><a href="file:///\\wsl$\Ubuntu\home\jerson\Holberton\rltoken\WCjn8NgohbQ5NGXEObWZvQ" title="Rubular is your best friend" target="_blank">Rubular is your best friend</a> </li>
<li><a href="file:///\\wsl$\Ubuntu\home\jerson\Holberton\rltoken\Zfvv_ydOCvJ_YaBB6eDqVw" title="Use a regular expression against a problem: now you have 2 problems" target="_blank">Use a regular expression against a problem: now you have 2 problems</a> </li>
<li><a href="file:///\\wsl$\Ubuntu\home\jerson\Holberton\rltoken\Y-OVGcJ5cskdXWIBowiE_A" title="Learn Regular Expressions with simple, interactive exercises" target="_blank">Learn Regular Expressions with simple, interactive exercises</a> </li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li><strong>All your script files must be executable</strong></li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env ruby</code></li>
<li>All your regex must be built for the Oniguruma library</li>
</ul>
  </div>
</div>

  
  
      <label for="quiz-answer-1506447957526">
    


  
  <label for="quiz-answer-1506447966080">
    


  
  <label for="quiz-answer-1506447975582">
    




  
  <label for="quiz-answer-1506447990910">
    


  
  <label for="quiz-answer-1506448010238">
    


  
  <label for="quiz-answer-1506448016293">
    




  
  <label for="quiz-answer-1506448055190">
    


  
  <label for="quiz-answer-1506448057879">
    




  


  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Simply matching School
    </h3>

  </div>
  <div class="panel-body">
    <span id="user_id" data-id="4579"></span>

<p>Requirements:</p>
<ul>
<li>The regular expression must match <code>School</code></li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>
<p>Example:</p>
<pre class="language-text">sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
</pre>
  </div>
  
  <!-- Panel footer - Controls -->
  

<p><span id="user_id" data-id="4579"></span></p>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Repetition Token #0
    </h3>

  </div>
  <div class="panel-body">
    <span id="user_id" data-id="4579"></span>

<p>Requirements:</p>
<ul>
<li>Find the regular expression that will match the above cases</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>
  </div>
  
  <!-- Panel footer - Controls -->
  

<p><span id="user_id" data-id="4579"></span></p>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Repetition Token #1
    </h3>

  </div>
  <div class="panel-body">
    <span id="user_id" data-id="4579"></span>

<p>Requirements:</p>
<ul>
<li>Find the regular expression that will match the above cases</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>
  </div>
  
  <!-- Panel footer - Controls -->
  

<p><span id="user_id" data-id="4579"></span></p>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Repetition Token #2
    </h3>

  </div>
  <div class="panel-body">
    <span id="user_id" data-id="4579"></span>

<p>Requirements:</p>
<ul>
<li>Find the regular expression that will match the above cases</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>
  </div>
  <div class="list-group">
    <!-- Task URLs -->

  </div>
  <!-- Panel footer - Controls -->
  

<p><span id="user_id" data-id="4579"></span></p>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Repetition Token #3
    </h3>

  </div>
  <div class="panel-body">
    <span id="user_id" data-id="4579"></span>

<p>Requirements:</p>
<ul>
<li>Find the regular expression that will match the above cases</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
<li>Your regex should not contain square brackets</li>
</ul>
  </div>
  
  <!-- Panel footer - Controls -->
  

<p><span id="user_id" data-id="4579"></span></p>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Not quite HBTN yet
    </h3>

  </div>
  <p>Requirements:</p><div class="panel-body">
    <span id="user_id" data-id="4579"><div></div></span>

<ul>
<li>The regular expression must be exactly matching a string that starts with <code>h</code> ends with <code>n</code> and can have any single character in between</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>
<p>Example:</p>
<pre class="language-text">sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$
</pre>
  </div>
  
  <!-- Panel footer - Controls -->
  

<p><span id="user_id" data-id="4579"></span></p>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Call me maybe
    </h3>

  </div>
  <div class="panel-body">
    <span id="user_id" data-id="4579"></span>

<p>Requirement:</p>
<ul>
<li>The regular expression must match a 10 digit phone number</li>
</ul>
<p>Example:</p>
<pre class="language-text">sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$
</pre>
  </div>
  
  <!-- Panel footer - Controls -->
  

<p><span id="user_id" data-id="4579"></span></p>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. OMG WHY ARE YOU SHOUTING?
    </h3>

  </div>
  <div class="panel-body">
    <span id="user_id" data-id="4579"></span>

<p>Requirement:</p>
<ul>
<li>The regular expression must be only matching: capital letters</li>
</ul>
<p>Example:</p>
<pre class="language-text">sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$
</pre>
  </div>
  
  <!-- Panel footer - Controls -->
  

  




<div class="modal fade users-done-modal" id="task-115-users-done-modal" data-task-id="115" data-project-id="78" style="display: none;">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "0. Simply matching School"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group"><p style="text-align: left;"><b>My peers:</b></p><div class="user" data-user-id="4562"><div><code>4562</code><span class="full_name"> Cesar Martinez</span><a class="user-preview-social email" target="_blank" href="mailto:cesar.martinez@holbertonschool.com"><i class="fa fa-envelope"></i></a><a class="user-preview-social personal_email" target="_blank" href="mailto:logisticacultura91@gmail.com"><i class="fa fa-envelope"></i></a><a class="slack" target="_blank" href="file:///\\wsl$\Ubuntu\home\jerson\Holberton\holberton-system_engineering-devops\0x06-regular_expressions\slack:\user?team=T0ENXA7A8&amp;id=U02V28B1MNH"><i class="fa fa-slack"></i></a><a class="user-preview-social twitter" target="_blank" href="https://twitter.com/cesarma50472117"><i class="fa fa-twitter"></i></a><span class="batch">cohort BOG-0122</span></div></div><p style="text-align: left; margin-top: 20px;"><b>From other cohorts:</b></p><input type="submit" name="commit" value="Load from other cohorts" class="btn btn-primary users_done_for_task_all" data-task-id="<%= task.id %>"></div>
            <div class="spinner" style="display: none;">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error" style="display: none;"></div>
        </div>
        </div>
    </div>
</div>
