# ARORA-Server-2
ARORA server with Django 2

<h1>This document introduces how to access this API</h1>

<h2>General Inforamtion</h2>
<ul>
<li> All responses are in Json format.</li>

</ul>

<h2>How to Get/Use a Token</h2>
<h5>1. Use your registered username and password to get your token</h5>
<ul>
<li><b>URL:</b> /api-token-auth</li>
<li><b>Method:</b> POST</li>
<li><b>Request Head:</b> content-type: appplication/json &emsp;</li>
<li><b>Request Body:</b>
<pre>
<code>
        {
          "username":"&lt;YOUR_USERNAME&gt;"(e.g. "a123456"),
          "password":"&lt;YOUR_PASSWORD&gt;"(e.g. "a123456")
        }
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
        {
          "token":"&lt;YOUR_NEW_TOKEN&gt;",
          "user_id":&lt;YOUR_USER_ID&gt;(e.g. 1)
        }
</code>
</pre>
</li>

<li><b>Errors:</b>
<ol>

<li>400 Bad Request
<pre>
<code>
    {
      "username":[
        "This field is required."
      ]
    }
</code>
</pre>
</li>

<li>400 Bad Request
<pre>
<code>
    {
      "password":[
        "This field is required."
      ]
    }
</code>
</pre>
</li>

<li>400 Bad Request
<pre>
<code>
        {
          "username":[
            "This field is required."
          ],
          "password":[
            "This field is required."
          ]
        }
</code>
</pre>
</li>

<li>400 Bad Request
<pre>
<code>
    {
      "non_field_errors":[
        "Unable to log in with provided credentials."
      ]
    }
</code>
</pre>
</li>
</ol>
</li>
</ul>

<h5>Once you get your token, you can use it on all requests.</h5>
<h5>2. You can use end-point: /api-token-verify to verify your token.</h5>
<ul>
<li><b>URL:</b> /api-token-verify</li>
<li><b>Method:</b> POST</li>
<li><b>Request Head:</b> content-type: appplication/json &emsp;</li>
<li><b>Request Body:</b>
<pre>
<code>
        {
          "token":"&lt;EXISTING_TOKEN&gt;"
        }
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
        {
          "token":"&lt;YOUR_TOKEN&gt;",
          "user_id":&lt;YOUR_USER_ID&gt;(e.g. 1)
        }
</code>
</pre>
</li>

<li><b>Errors:</b>
<ol>

<li>400 Bad Request
<pre>
<code>
    {
        "non_field_errors": [
            "Signature has expired."
        ]
    }
</code>
</pre>
</li>

<li>400 Bad Request
<pre>
<code>
    {
        "non_field_errors": [
            "Error decoding signature."
        ]
    }
</code>
</pre>
</li>

<li>400 Bad Request
<pre>
<code>
    {
        "token": [
            "This field may not be blank."
        ]
    }
</code>
</pre>
</li>

</ol>
</li>
</ul>

<h5>3. You can use end-point: /api-token-refresh to refresh your token's expiration time. But please remember set JWT_REFRESH
= TRUE, for more details, <a href="http://getblimp.github.io/django-rest-framework-jwt/">JWT API Document</a></h5>
<ul>
<li><b>URL:</b> /api-token-refresh</li>
<li><b>Method:</b> POST</li>
<li><b>Request Head:</b> content-type: appplication/json &emsp;</li>
<li><b>Request Body:</b>
<pre>
<code>
        {
          "token":"&lt;EXISTING_TOKEN&gt;"
        }
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
        {
          "token":"&lt;YOUR_NEW_TOKEN&gt;"
        }
</code>
</pre>
</li>

<li><b>Errors:</b>
<ol>

<li>400 Bad Request
<pre>
<code>
    {
        "non_field_errors": [
            "orig_iat field is required."
        ]
    }
</code>
</pre>
</li>

<li>400 Bad Request
<pre>
<code>
   {
        "non_field_errors": [
            "Signature has expired."
        ]
   }
</code>
</pre>
</li>

<li>400 Bad Request
<pre>
<code>
    {
        "non_field_errors": [
            "Error decoding signature."
        ]
    }
</code>
</pre>
</li>

</ol>
</li>
</ul>


<h2>End-Points</h2>
<!-- *************************************************************************************** -->
<h3>Users</h3>
<ol>
<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/user
</h4>
<ul>

<li><b>URL:</b> /user/&lt;int:user_id&gt;</li>

<li><b>Method:</b> GET</li>

<li><b>Request Head:</b> Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
<b>None</b>
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "user_id": &lt;USER_ID&gt;,
    "user_name": "&lt;USER_NAME&gt;",
    "user_current_mood": &lt;USER_CURRENT_MOOD&gt;,
    "user_current_mood_updated": "&lt;USER_CURRENT_MOOD_UPDATED&gt;",
    "user_current_location_lat": "&lt;USER_CURRENT_LOCATION_LATITUDE&gt;",
    "user_current_location_long": "&ltUSER_CURRENT_LOCATION_LONGITUDE;&gt;",
    "user_current_location_updated": "&lt;USER_CURRENT_LOCATION_UPDATED&gt;",
    "user_score": &lt;USER_SCORE&gt;,
}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "User does not exist"
}
</code>
</pre>
</li>

</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->
<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/user
</h4>
<ul>

<li><b>URL:</b> /user</li>

<li><b>Method:</b> POST</li>

<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
{
    "username":"&lt;USER_NAME&gt;",
    "email":"&lt;EMAIL&gt;",
    "password": "&lt;PASSWORD&gt;"
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "user_id": &lt;USER_ID&gt;
}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>

<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>


<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>409 Conflict
<pre>
<code>
{
    "error": "User already exists with this user name"
}
</code>
</pre>
</li>

<li>409 Conflict
<pre>
<code>
{
    "error": "User already exists with this email"
}
</code>
</pre>
</li>


</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->
<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/userinfo/users
</h4>
<ul>

<li><b>URL:</b> /users</li>

<li><b>Method:</b> GET</li>

<li><b>Request Head:</b> Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
<b>None</b>
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
[
    {
        "user_id": &lt;USER_ID&gt;,
        "user_name": "&lt;USER_NAME&gt;",
        "user_current_mood": &lt;USER_CURRENT_MOOD&gt;,
        "user_current_mood_updated": "&lt;USER_CURRENT_MOOD_UPDATED&gt;",
        "user_current_location_lat": "&lt;USER_CURRENT_LOCATION_LATITUDE&gt;",
        "user_current_location_long": "&ltUSER_CURRENT_LOCATION_LONGITUDE;&gt;",
        "user_current_location_updated": "&lt;USER_CURRENT_LOCATION_UPDATED&gt;",
        "user_score": &lt;USER_SCORE&gt;,
    },
    ...
]
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->
<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/nearby_users
</h4>
<ul>

<li><b>URL:</b> /nearby_users</li>

<li><b>Method:</b> GET</li>

<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
</code>
{
    "user_id": &lt;USER_ID&gt;
}
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "user_id ": &lt;USER_ID&gt;,
    "user_current_lat": &lt;USER_CURRENT_LATITUDE&gt;,
    "user_current_lng": &lt;USER_CURRENT_LONGITUDE&gt;
}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>

<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "User does not exist"
}
</code>
</pre>
</li>
</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->
</ol>
<!-- *************************************************************************************** -->

<!-- *************************************************************************************** -->
<h3>Quests</h3>
<ol>

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/quest/quest
</h4>
<ul>
<li><b>URL:</b> /quest</li>

<li><b>Method:</b> GET</li>

<li><b>Request Head:</b> Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
{
	"quest_id":&lt;QUEST_ID&gt;
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "quest_id": &lt;QUEST_ID&gt;,
    "quest_type_id": &lt;QUEST_TYPE_ID&gt;,
    "quest_status": &lt;QUEST_STATUS&gt;
}
</code>
</pre>
</li>

<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "Quest does not exist"
}
</code>
</pre>
</li>

<li>409 Conflict
<pre>
<code>
{
    "error": "Quest type is invalid"
}
</code>
</pre>
</li>

</ol>
</li>

</ul>
</li>
<!-- _______________________________________________________________________________________ -->

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/quest
</h4>
<ul>
<li><b>URL:</b> /quest</li>

<li><b>Method:</b> POST</li>

<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
{
	"quest_type_id":&lt;QUEST_TYPE_ID&gt;,
	"quest_status": &lt;QUEST_STATUS&gt
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "quest_id": &lt;QUEST_ID&gt;
}
</code>
</pre>
</li>

<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "Quest does not exist"
}
</code>
</pre>
</li>

<li>409 Conflict
<pre>
<code>
{
    "error": "Quest type is invalid"
}
</code>
</pre>
</li>
</ol>
</li>

</ul>
</li>
<!-- _______________________________________________________________________________________ -->

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/quest
</h4>
<ul>
<li><b>URL:</b> /quest</li>

<li><b>Method:</b> PUT</li>

<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
{
    "quest_id": &lt;QUEST_ID&gt;,
    "quest_type_id": &lt;QUEST_TYPE_ID&gt;,
    "quest_status": &lt;QUEST_STATUS&gt;
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "quest_id": &lt;QUEST_ID&gt;
}
</code>
</pre>
</li>

<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "Quest does not exist"
}
</code>
</pre>
</li>

<li>409 Conflict
<pre>
<code>
{
    "error": "Quest type is invalid"
}
</code>
</pre>
</li>
</ol>
</li>

</ul>
</li>
<!-- _______________________________________________________________________________________ -->

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/quests
</h4>
<ul>
<li><b>URL:</b> /quests</li>

<li><b>Method:</b> GET</li>

<li><b>Request Head:</b> Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
<b>None</b>
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
[
    {
        "quest_id": &lt;QUEST_ID&gt;,
        "quest_type_id": &lt;QUEST_TYPE_ID&gt;,
        "quest_status": &lt;QUEST_STATUS&gt;
    },
    ...
]
</code>
</pre>
</li>

<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "Quest does not exist"
}
</code>
</pre>
</li>
</ol>
</li>

</ul>
</li>
<!-- _______________________________________________________________________________________ -->
</ol>
<!-- *************************************************************************************** -->

<!-- *************************************************************************************** -->
<h3>Location Reports</h3>
<ol>
<li>

<h4>
/locationreport
</h4>

<ul>

<li><b>URL:</b> /locationreport</li>

<li><b>Method:</b> POST</li>

<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
{
	"latitude": &lt;LATITUDE&gt,
	"longitude": &lt;LONGITUDE&gt
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "location_report_id":&lt;LOCATION_REPORT_ID&gt;
}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>
</ol>
</li>
</ul>
</li>
</ol>
<!-- *************************************************************************************** -->

<!-- *************************************************************************************** -->
<h3>Mood Reports</h3>
<ol>
<li>
<h4>
/moodreport
</h4>
<ul>

<li><b>URL:</b> /moodreport</li>

<li><b>Method:</b> POST</li>

<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
{
	"user_mood": &lt;USER_MOOD&gt;,
	"user_text": "&lt;USER_TEXT&gt;"
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "mood_report_id": &lt;MOOD_REPORT_ID&gt;
}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>
</ol>
</li>
</ul>
</li>
</ol>
<!-- *************************************************************************************** -->




<!-- *************************************************************************************** -->
<h3>Quest Reports</h3>
<ol>
<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/questreport/&lt;QUEST_REPORT_ID&gt;
</h4>
<ul>
<li><b>URL:</b> /questreport/&lt;QUEST_REPORT_ID&gt;</li>

<li><b>Method:</b> GET</li>

<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
{
	"quest_report_id":&lt;QUEST_REPORT_ID&gt;
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "quest_report_id": &lt;QUEST_REPORT_ID&gt;,
    "quest_id": &lt;QUEST_ID&gt,
    "user_id": &lt;USER_ID&gt,
    "quest_started_at": "&lt;QUEST_STARTED_AT&gt;",  (e.g. "2019-02-22T09:30:05.609728Z")
    "quest_ended_at": "&lt;QUEST_ENDED_AT&gt;"
}
</code>
</pre>
</li>

<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "Quest report does not exist"
}
</code>
</pre>
</li>
</ol>
</li>

</ul>
</li>
<!-- _______________________________________________________________________________________ -->

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/quest/questreport
</h4>
<ul>
<li><b>URL:</b> /quest/questreport</li>

<li><b>Method:</b> POST</li>

<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
{
	"quest_id": &lt;QUEST_ID&gt;
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "quest_report_id": &lt;QUEST_REPORT_ID&gt;
}
</code>
</pre>
</li>

<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "Quest does not exist"
}
</code>
</pre>
</li>


<li>409 Conflict
<pre>
<code>
{
    "error": "Quest report has existed"
}
</code>
</pre>
</li>
</ol>
</li>

</ul>
</li>
<!-- _______________________________________________________________________________________ -->

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/quest/questreport
</h4>
<ul>
<li><b>URL:</b> /quest/questreport</li>

<li><b>Method:</b> PUT</li>

<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
{
    "quest_id": &lt;QUEST_ID&gt;
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "quest_report_id": &lt;QUEST_REPORT_ID&gt;
}
</code>
</pre>
</li>

<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>400 Bad Request
<pre>
<code>
{
    "error": "Invalid user behavior"
}
</code>
</pre>
</li>


<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>

<li>404 Not Found
<pre>
<code>
{
    "error": "Quest report does not exist"
}
</code>
</pre>

</ol>
</li>

</ul>
</li>
<!-- _______________________________________________________________________________________ -->

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/quest/questreports
</h4>
<ul>
<li><b>URL:</b> /quest/questreports</li>

<li><b>Method:</b> GET</li>

<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
<b>None</b>
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
[
    {
        "quest_report_id": &lt;QUEST_REPORT_ID&gt;,
        "quest_id": &lt;QUEST_ID&gt,
        "user_id": &lt;USER_ID&gt,
        "quest_started_at": "&lt;QUEST_STARTED_AT&gt;",  (e.g. "2019-02-22T09:30:05.609728Z")
        "quest_ended_at": "&lt;QUEST_ENDED_AT&gt;"
    },
    ...
]
</code>
</pre>
</li>

<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "Quest report does not exist"
}
</code>
</pre>

</ol>
</li>

</ul>
</li>
<!-- _______________________________________________________________________________________ -->
</ol>
<!-- *************************************************************************************** -->




<!-- *************************************************************************************** -->
<h3>System Reports</h3>
<ol>
<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/systemreport/systemreport
</h4>
<ul>
<li><b>URL:</b> /systemreport/systemreport</li>
<li><b>Method:</b> POST</li>
<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>
<li><b>Request Body:</b>
<pre>
<code>
{
	"user_id": &lt;USER_ID&gt;,
	"power_level":&lt;POWER_LEVEL&gt;,
	"request_latency":&lt;REQUEST_LATENCY&gt;
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
	"system_report_id": &lt;SYSTEM_REPORT_ID&gt;
}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>
</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->
</ol>
<!-- *************************************************************************************** -->




<!-- *************************************************************************************** -->
<h3>Baseline Reports - TBD</h3>
<ol>
<li>
<h4>
<b>TBD</b>
</h4>

<ul>

<li><b>URL:</b> <b>TBD</b></li>

<li><b>Method:</b> <b>TBD</b></li>

<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
<b>TBD</b>
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
<b>TBD</b>
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li><b>TBD</b></li>
<!--<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<!--<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<!--<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li> 
-->
</ol>
</li>
</ul>
</li>
</ol>

<!-- *************************************************************************************** --> 






<!-- *************************************************************************************** -->
<h3>User Interactions</h3>
<ol>
<li>

<h4>
/userinteraction/userinteraction
</h4>

<ul>

<li><b>URL:</b> /userinteraction/userinteraction</li>

<li><b>Method:</b> POST</li>

<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>

<li><b>Request Body:</b>
<pre>
<code>
{
     "recipient_user_id": &lt;RECIPIENT_USER_ID&gt;,
     "interaction_type": &lt;INTERACTION_TYPE&gt;,
     "content": "&lt;CONTENT&gt;"
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
     "user_interaction_id": &lt;USER_INTERACTION_ID&gt;
}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>
</ol>
</li>
</ul>
</li>
</ol>
<!-- *************************************************************************************** -->



<!-- *************************************************************************************** -->
<h3>UserButterflies</h3>
<ol>
<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/butterfly/userbutterfly
</h4>
<ul>
<li><b>URL:</b> /butterfly/userbutterfly</li>
<li><b>Method:</b> GET</li>
<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>
<li><b>Request Body:</b>
<pre>
<code>
{
    "user_butterfly_id":&lt;USER_BUTTERFLY_ID&gt;
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "user_butterfly_id": &lt;USER_BUTTERFLY_ID&gt;,
    "butterfly_id": &lt;BUTTERFLY_ID&gt,
    "user_id": &lt;USER_ID&gt,
    "time_caught": "&lt;TIME_CAUGHT&gt;"  (e.g. 2019-02-23T09:38:42.925706Z)
}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>401 Not Found
<pre>
<code>
{
    "error": "User butterfly does not exist"
}
</code>
</pre>
</li>
</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/butterfly/userbutterfly
</h4>
<ul>
<li><b>URL:</b> /butterfly/userbutterfly</li>
<li><b>Method:</b> POST</li>
<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>
<li><b>Request Body:</b>
<pre>
<code>
{
     "user_id":&lt;USER_ID&gt,
     "butterfly_id":&lt;BUTTERFLY_ID&gt,
     "time_caught":"&lt;TIME_CAUGHT&gt;" (e.g. 2019-02-23T09:38:42.925706Z)
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
     "user_butterfly_id": &lt;USER_BUTTERFLY_ID&gt;
}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>409 Conflict
<pre>
<code>
{
    "error": "Time_caught invalid"
}
</code>
</pre>
</li>

<li>409 Conflict
<pre>
<code>
{
    "error": "Butterfly_id invalid"
}
</code>
</pre>
</li>

<li>409 Conflict
<pre>
<code>
{
    "error": "User_id invalid"
}
</code>
</pre>
</li>
</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/butterfly/userbutterfly
</h4>
<ul>
<li><b>URL:</b> /butterfly/userbutterfly</li>
<li><b>Method:</b> PUT</li>
<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>
<li><b>Request Body:</b>
<pre>
<code>
{
     "user_butterfly_id":&lt;USER_BUTTERFLY_ID&gt;,
     "user_id":&lt;USER_ID&gt,
     "butterfly_id":&lt;BUTTERFLY_ID&gt,
     "time_caught":"&lt;TIME_CAUGHT&gt;" (e.g. 2019-02-23T09:38:42.925706Z)
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "user_butterfly_id":&lt;USER_BUTTERFLY_ID&gt;
}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "error": "Permission denied"
}
</code>
</pre>
</li>


<li>409 Conflict
<pre>
<code>
{
    "error": "Butterfly_id invalid"
}
</code>
</pre>
</li>

<li>409 Conflict
<pre>
<code>
{
    "error": "User_id invalid"
}
</code>
</pre>
</li>

<li>409 Conflict
<pre>
<code>
{
    "error": "Time_caught invalid"
}
</code>
</pre>
</li>

</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/butterfly/userbutterfly
</h4>
<ul>
<li><b>URL:</b> /butterfly/userbutterfly</li>
<li><b>Method:</b> DELETE</li>
<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>
<li><b>Request Body:</b>
<pre>
<code>
{
    "user_butterfly_id":&lt;USER_BUTTERFLY_ID&gt;
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "User_butterfly_id does not exist"
}
</code>
</pre>
</li>
</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/butterfly/userbutterflies
</h4>
<ul>
<li><b>URL:</b> /butterfly/userbutterflies</li>
<li><b>Method:</b> GET</li>
<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>
<li><b>Request Body:</b>
<pre>
<code>
<b>None</b>
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
[
    {
        "user_butterfly_id": &lt;USER_BUTTERFLY_ID&gt;,
        "butterfly_id": &lt;BUTTERFLY_ID&gt;,
        "user_id": &lt;USER_ID&gt;,
        "time_caught": "&lt;TIME_CAUGHT&gt;"
    },
    ...
]
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "User_butterfly_id does not exist" 
}
</code>
</pre>
</li>
</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->
</ol>
<!-- *************************************************************************************** -->





<!-- *************************************************************************************** -->
<h3>Butterflies</h3>
<ol>
<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/butterfly/butterfly
</h4>
<ul>
<li><b>URL:</b> /butterfly/butterfly</li>
<li><b>Method:</b> GET</li>
<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>
<li><b>Request Body:</b>
<pre>
<code>
{
	"butterfly_id": &lt;BUTTERFLY_ID&gt;
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "butterfly_id": &lt;BUTTERFLY_ID&gt;,
    "butterfly_type_id": &lt;BUTTERFLY_TYPE_ID&gt;,
    "butterfly_create_at": "&lt;BUTTERFLY_CREATE_AT&gt;"
}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "Butterfly does not exist"
}
</code>
</pre>
</li>
</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/butterfly/butterfly
</h4>
<ul>
<li><b>URL:</b> /butterfly/butterfly</li>
<li><b>Method:</b> POST</li>
<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>
<li><b>Request Body:</b>
<pre>
<code>
{
    "butterfly_type_id" : &lt;BUTTERFLY_TYPE_ID&gt;
}
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
{
    "butterfly_id": &lt;BUTTERFLY_ID&gt;
}
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>409 Conflict
<pre>
<code>
{
    "error": "Butterfly_type invalid"
}
</code>
</pre>
</li>
</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->

<!-- _______________________________________________________________________________________ -->
<li>
<h4>
/butterfly/butterflies
</h4>
<ul>
<li><b>URL:</b> /butterfly/butterflies</li>
<li><b>Method:</b> GET</li>
<li><b>Request Head:</b> content-type: appplication/json;&emsp;Authorization: JWT &lt;YOUR_TOKEN&gt;</li>
<li><b>Request Body:</b>
<pre>
<code>
<b>None</b>
</code>
</pre>
</li>

<li><b>Response:</b>
<pre>
<code>
[
    {
        "butterfly_id": &lt;BUTTERFLY_ID&gt;,
        "butterfly_type_id": &lt;BUTTERFLY_TYPE_ID&gt;,
        "butterfly_create_at": "&lt;BUTTERFLY_CREATE_AT&gt;"
    },
    ...
]
</code>
</pre>
</li>
<li><b>Errors:</b>
<ol>
<li>400 Bad Request
<pre>
<code>
{
    "error": "Wrong Json Format"
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Authentication credentials were not provided."
}
</code>
</pre>
</li>

<li>401 Unauthorized
<pre>
<code>
{
    "detail": "Signature has expired."
}
</code>
</pre>
</li>

<li>404 Not Found
<pre>
<code>
{
    "error": "Butterfly does not exist"
}
</code>
</pre>
</li>
</ol>
</li>
</ul>
</li>
<!-- _______________________________________________________________________________________ -->
</ol>
<!-- *************************************************************************************** -->


