
<h1 id="welcome-to-arora-server">Welcome to ARORA Server</h1>
<p>This is a server project based on <a href="%5Bhttps://www.django-rest-framework.org/%5D(https://www.django-rest-framework.org/)"><strong>Django REST Framework</strong></a>.</p>
<h1 id="package-dependency">Package Dependency</h1>
<ol>
<li>Django 2.2.1</li>
<li>djangorestframework 3.9.2</li>
<li>djangorestframework-jwt 1.11.0</li>
<li>rest-condtion 1.0.3</li>
</ol>
<h1 id="how-to-set-up-the-server">How to Set Up the Server</h1>
<ol>
<li>
<p>Get the project from Github</p>
</li>
<li>
<p>Go to /root_dir/arora/env, then run command: source ./active to active virtual environment.<br>
<img src="https://lh3.googleusercontent.com/Bw1KtpaUX7TlGxucETfjQyYWtq8SMZjMl9zjzU5nReRumaEsPttJYrJ5pgBs7E2u10l7bQFpPhk" alt="enable virtual environment"></p>
</li>
<li>
<p>Back to /root_dir</p>
</li>
<li>
<p>Create migration files for building database, sudo python3 <a href="http://manage.py">manage.py</a> makemigrations<br>
<img src="https://lh3.googleusercontent.com/gsOTJvpbbQMOaBIJChNb2ylIkk0XRjpVJ-kOBtG7w0tKqgSRF9BqvwC581JiiQkO5hfHIt6Ai4U" alt="make migrations"></p>
</li>
<li>
<p>Create a brand new database, sudo python3 <a href="http://manage.py">manage.py</a> migrate.<br>
<img src="https://lh3.googleusercontent.com/Gx63J9pzRTlrl0fJB-iHeosq7KUsWXvDLT_8OR6smoF1gwP2CUhfD_xT1yogC7R70WFCYlhji5k" alt="create database"></p>
</li>
<li>
<p>Create a super user for the first step to access database, sudo python3 <a href="http://manage.py">manage.py</a> createsuperuser.<br>
<img src="https://lh3.googleusercontent.com/zuB5mo0J4QtEMD8dzlmJCjoE1dlcDQJcaLc-YGUGMN_ooy-9uzhImRx13Wkem1X3kBt9M4PSkuE" alt="create super user"></p>
</li>
<li>
<p>Run server, sudo python3 runserver, or you can assign customized IP address and port here, sudo python3 runserver 127.0.0.1 8000.<br>
<img src="https://lh3.googleusercontent.com/zK1IcvohenI-2xqV-hT8KcpJWpsRRPMNo49HwLtW_hw7-oUOdPsn2SZThIYoinuQvblNX4pCsWY" alt="run server"></p>
</li>
<li>
<p>Open browser, go to 127.0.0.1:8000/admin to access admin site.<br>
<img src="https://lh3.googleusercontent.com/Rq6EcrMBmbcAXqv8IdKzRWlOGTf33hNk4g5x-2vPgBaJ5WOFT26WdBZnVeHGd27TzCJ5gnbgqxc" alt="log in admin site"></p>
</li>
<li>
<p>Log in with your super user account.</p>
</li>
<li>
<p>Now, you can manage database by your super user account. And we done. Have fun!<br>
<img src="https://lh3.googleusercontent.com/3n6j2ayXfIkAWPMONnrxjnPQCOOTMVdYq5PsAaroHup7dqrGkHW5rhS62kJB2F0lFxhST7OremQ" alt="admin site"></p>
</li>
</ol>
<p><strong>Note:</strong></p>
<ol>
<li>Using admin site is a optional way to manage your database.</li>
<li>If you meet any problem when you do the above process, please make sure nothing wrong with your migration files. <a href="https://github.com/LooDaHu/ARORA_General_Introduction/blob/master/README.md">Learn more.</a></li>
</ol>
<h1 id="models">Models</h1>
<ol>
<li>
<p>UserInfo<br>
|–&gt; user_info_id <em>(integer)</em>	<br>
|–&gt; user_id <em>(integer)</em>	<br>
|–&gt; user_name_of_strength* <em>(string)</em><br>
|–&gt; user_created_at <em>(datetime)</em><br>
|–&gt; user_current_mood* <em>(integer)</em>	<br>
|–&gt; user_current_mood_updated* <em>(datetime)</em><br>
|–&gt; user_current_location_lat* <em>(decimal)</em><br>
|–&gt; user_current_location_long* <em>(decimal)</em><br>
|–&gt; user_current_location_updated* <em>(datetime)</em><br>
|–&gt; user_current_butterfly* <em>(integer)</em>	<br>
|–&gt; user_pollen* <em>(integer)</em>	<br>
|–&gt; user_points* <em>(integer)</em>	<br>
<strong>|–&gt; username</strong> (Django bulit-in field) <em>(string)</em><br>
<strong>|–&gt; email</strong> (Django bulit-in field) <em>(string)</em><br>
<strong>|–&gt; password</strong> (Django bulit-in field) <em>(string)</em></p>
</li>
<li>
<p>ButterflyType<br>
|–&gt; butterfly_type_id <em>(integer)</em>	<br>
|–&gt; butterfly_type_description* <em>(integer)</em>	<br>
|–&gt; butterfly_type_image* <em>(string)</em></p>
</li>
<li>
<p>Butterfly<br>
|–&gt; butterfly_id <em>(integer)</em><br>
|–&gt; butterfly_type_id* <em>(integer)</em><br>
|–&gt; butterfly_create_at <em>(datetime)</em></p>
</li>
<li>
<p>UserButterfly<br>
|–&gt; user_butterfly_id <em>(integer)</em><br>
|–&gt; butterfly_id* <em>(integer)</em><br>
|–&gt; time_caught <em>(datetime)</em> (Record the date time when it is created)<br>
|–&gt; user_id* <em>(integer)</em></p>
</li>
<li>
<p>ButterflyLike<br>
|–&gt; butteefly_like_id <em>(integer)</em><br>
|–&gt; butterfly_id* <em>(integer)</em><br>
|–&gt; user_id* <em>(integer)</em><br>
|–&gt; like_created_at <em>(datetime)</em></p>
</li>
<li>
<p>ButterflyComment<br>
|–&gt; butterfly_comment_id  <em>(integer)</em><br>
|–&gt; butterfly_id*  <em>(integer)</em><br>
|–&gt; user_id*  <em>(integer)</em><br>
|–&gt; comment_created_at <em>(datetime)</em><br>
|–&gt; comment_text* <em>(string)</em></p>
</li>
<li>
<p>BaselineReport<br>
|–&gt; baseline_report_id <em>(integer)</em><br>
|–&gt; user_id* <em>(integer)</em><br>
|–&gt; baseline_report_created_at <em>(datetime)</em><br>
|–&gt; baseline_report_results* <em>(string)</em></p>
</li>
<li>
<p>LocationReport<br>
|–&gt; location_report_id <em>(integer)</em><br>
|–&gt; location_report_lat* <em>(decimal)</em><br>
|–&gt; location_report_long* <em>(decimal)</em>  location_report_create_at<br>
|–&gt; location_report_create_at <em>(datetime)</em><br>
|–&gt; user_id* <em>(integer)</em></p>
</li>
<li>
<p>MoodType<br>
|–&gt; mood_type_id <em>(integer)</em><br>
|–&gt; mood_type_description* <em>(string)</em></p>
</li>
<li>
<p>MoodReport<br>
|–&gt; mood_report_id <em>(integer)</em><br>
|–&gt; mood_report_created_at<br>
|–&gt; user_id* <em>(integer)</em><br>
|–&gt; mood_type* <em>(integer)</em><br>
|–&gt; user_text* <em>(string)</em></p>
</li>
<li>
<p>Phrase<br>
|–&gt; phrase_id <em>(integer)</em><br>
|–&gt; phrase_english_text* <em>(string)</em><br>
|–&gt; phrase_indigenous_text* <em>(string)</em></p>
</li>
<li>
<p>QuestType<br>
|–&gt; quest_type_id <em>(integer)</em><br>
|–&gt; quest_type_description* <em>(string)</em></p>
</li>
<li>
<p>QuestStatus<br>
|–&gt; quest_status_id <em>(integer)</em><br>
|–&gt; quest_status_description* <em>(string)</em></p>
</li>
<li>
<p>Quest<br>
|–&gt; quest_id <em>(integer)</em><br>
|–&gt; quest_type_id* <em>(integer)</em><br>
|–&gt; quest_status_id* <em>(integer)</em></p>
</li>
<li>
<p>QuestReport<br>
|–&gt; quest_report_id <em>(integer)</em><br>
|–&gt; quest_id* <em>(integer)</em><br>
|–&gt; user_id* <em>(integer)</em><br>
|–&gt; quest_started_at <em>(datetime)</em><br>
|–&gt; quest_ended_at <em>(datetime)</em> (Record the date time when it is updated)</p>
</li>
<li>
<p>SystemReport<br>
|–&gt; system_report_id <em>(integer)</em><br>
|–&gt; user_id* <em>(integer)</em><br>
|–&gt; power_level* <em>(integer)</em><br>
|–&gt; request_latnecy* <em>(string)</em><br>
|–&gt; system_report_created_at <em>(datetime)</em></p>
</li>
<li>
<p>UserInteractionType<br>
|–&gt; user_interaction_type_id <em>(integer)</em><br>
|–&gt; user_interaction_description* <em>(string)</em></p>
</li>
<li>
<p>UserInteraction<br>
|–&gt; user_interaction_id <em>(integer)</em><br>
|–&gt; user_interaction_created_at <em>(datetime)</em><br>
|–&gt; initator_user_id* <em>(integer)</em><br>
|–&gt; receiver_user_id* <em>(integer)</em><br>
|–&gt; user_interaction_type_id* <em>(integer)</em><br>
|–&gt; user_interaction_content* <em>(string)</em></p>
|-&gt; quest_report_id* <em>(integer)</em></p>
</li>
</ol>
<p><strong>Note:</strong></p>
<ol>
<li>
<p>This is a liitle special for creating a new user, due to use default django user model:</p>
<blockquote>
<p>Method: POST<br>
DATA in JSON:	{  “username”: “&lt; user_name &gt;”, “password”: “&lt; password &gt;”, “email”: “&lt; email &gt;” }</p>
</blockquote>
</li>
<li>
<p>The server returns all fields in the models back when it gets a <strong>GET</strong> request.</p>
</li>
<li>
<p>The fields in the models wtih <strong>star</strong> notation are entirely requried at <strong>POST/PUT</strong> request.</p>
</li>
<li>
<p>The fields in the models wtih <strong>star</strong> notation are partially requried at <strong>PATCH</strong> request.</p>
</li>
<li>
<p>There are two situation for non-requried field( the fields without <strong>star</strong> notation):<br>
(1) The field is a prime key, such as, user_info_id, quest_id, and mood_report_id.<br>
(2) The field is a date time field which is created or updated, such as, time_caught, location_report_create_at, and quest_ended_at.</p>
</li>
<li>
<p>The source code reserves all the right for the final explanation.</p>
</li>
</ol>
<h1 id="endpoints-url">Endpoints URL</h1>
<p><strong>General URL Principle:</strong><br>
POST:  &lt; DOMAIN_NAME or IP_ADDRESS &gt;/&lt; RESOURCE_NAME &gt;<br>
e.g: <a href="http://127.0.0.1:8000/userinfo">http://127.0.0.1:8000/userinfo</a></p>
<p>GET:  &lt; DOMAIN_NAME or IP_ADDRESS &gt;/&lt; RESOURCE_NAME &gt;/&lt; RETRIEVED_ITEM_ID &gt;<br>
e.g: <a href="http://127.0.0.1:8000/userinfo/1">http://127.0.0.1:8000/userinfo/1</a></p>
<p>GET(All items):  &lt; DOMAIN_NAME or IP_ADDRESS &gt;/&lt; RESOURCE_NAME s&gt;/&lt; RETRIEVED_ITEM_ID &gt;<br>
e.g: <a href="http://127.0.0.1:8000/quests">http://127.0.0.1:8000/quests</a>	<a href="http://127.0.0.1:8000/phrases">http://127.0.0.1:8000/phrases</a></p>
<p>PUT:  &lt; DOMAIN_NAME or IP_ADDRESS &gt;/&lt; RESOURCE_NAME &gt;/&lt; UPDATED_ITEM_ID &gt;<br>
e.g: <a href="http://127.0.0.1:8000/quest/1">http://127.0.0.1:8000/quest/1</a></p>
<p>PATCH:  &lt; DOMAIN_NAME or IP_ADDRESS &gt;/&lt; RESOURCE_NANE &gt;/&lt; UPDATED_ITEM_ID &gt;<br>
e.g: <a href="http://127.0.0.1:8000/userinteraction/1">http://127.0.0.1:8000/userinteraction/1</a></p>
<p>DELETE:  &lt; DOMAIN_NAME or IP_ADDRESS &gt;/&lt; RESOURCE_NAME &gt;/&lt; DELETED_ITEM_ID &gt;<br>
e.g: <a href="http://127.0.0.1:8000/userbutterfly/1">http://127.0.0.1:8000/userbutterfly/1</a></p>

<table>
<thead>
<tr>
<th>Model  Name</th>
<th>Resource Name</th>
<th>Accept Method</th>
</tr>
</thead>
<tbody>
<tr>
<td>UserInfo</td>
<td>userinfo</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>UserInfo</td>
<td>nearbyusers</td>
<td>GET</td>
</tr>
<tr>
<td>ButterflyType</td>
<td>butterflytype</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>Butterfly</td>
<td>butterfly</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>UserButterfly</td>
<td>userbutterfly</td>
<td>POST; GET; PUT; PATCH; DELETE</td>
</tr>
<tr>
<td>ButterflyLike</td>
<td>butterflylike</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>ButterflyComment</td>
<td>butterflycomment</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>BaselineReport</td>
<td>baselinereport</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>LocationReport</td>
<td>locationreport</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>MoodType</td>
<td>moodtype</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>MoodReport</td>
<td>moodreport</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>Phrase</td>
<td>phrase</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>Quest</td>
<td>quest</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>QuestType</td>
<td>questtype</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>QuestStatus</td>
<td>queststatus</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>QuestReport</td>
<td>questreport</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>SystemReport</td>
<td>systemreport</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>UserInteractionType</td>
<td>userinteractiontype</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
<tr>
<td>UserInteraction</td>
<td>userinteraction</td>
<td>POST; GET; PUT; PATCH</td>
</tr>
</tbody>
</table><p>Here I recommend you use <a href="https://www.getpostman.com/">POSTMAN</a>, a API development environemnt, to test the endpoints and know how to access those endpoints more directly.  And I have a collection contains all useage of the endpoints, which could let us have a easier life.<br>
Sharing Link: <a href="https://www.getpostman.com/collections/921a12a8fa5a925e0c28">https://www.getpostman.com/collections/921a12a8fa5a925e0c28</a></p>
<p>A Example of How to Use:</p>
<ol>
<li>
<p>Afer you have installed and opened POSTMAN. Click <strong>Import</strong> button. Let’s start importing the collection.<br>
<img src="https://lh3.googleusercontent.com/Gci7dTi8HgkLNpWV2KqtIAVc-j_R6NAik1XxExxPPoBwzOPNPkY8U74GGrpFvhfN1_Qbzz5y5oo" alt="Start Import"></p>
</li>
<li>
<p>Choose  <strong>Import From Link</strong>, then Copy the <strong>Sharing Link</strong> to it.<br>
<img src="https://lh3.googleusercontent.com/JlzR-r-MiwopjfVo76Dh7dJ0aWlp3Ot5TjHDx9I4FzFNhY4i1B12fQ039QFkXhqsRglbvMD42Z4" alt="enter the link"></p>
</li>
<li>
<p>After you sucessfully import the collection, you can see the pop-up at the downside.<br>
<img src="https://lh3.googleusercontent.com/64N10xjIrToHyojpIgPxPUMGksGjE2x3-97-egofgdoXcidgyNSgfWSqqOr-4R4Pk9oXCpP0KLQ" alt="enter image description here"></p>
</li>
<li>
<p>Let’s try to create a user. Of cource, please make sure the server is running properly. And the set-up of the request should be correct aslo.<br>
<img src="https://lh3.googleusercontent.com/mNlVFji4zcPImau9Qb330wUWH4wjlfqdNZ5w0BEhkpI7hQscckLv0bfllXt7rMqn2uRuwRaP6js" alt="correct set-up 1"><br>
<img src="https://lh3.googleusercontent.com/8NY5rhCEo7lDZHRAjAMBtk7Nmj-Mxn1hxVExeZxpR27-8Hffph5smutQ92uZYsSoO0dd2ftrvnM" alt="correct set-up 2"></p>
</li>
<li>
<p>After every thing is ok, Click the <strong>Send</strong> button. And we get a response shows the user_id of our new user back.<br>
<img src="https://lh3.googleusercontent.com/ZQteAq437kU8-0D2uc4Ly5_K5mAXoB6XqzuXNcEZ9hjKXb8jXDEhOm7g95zwrnc9K378t14AEts" alt="enter image description here"></p>
</li>
</ol>
<h1 id="foreign-key-relationship-map">Foreign Key Relationship Map</h1>
<p><img src="https://lh3.googleusercontent.com/HHVpXfdrQpsn6Dni90zc--UU-BtoxjyRfuMlX4MvEHtv-bCBolApN5uc_gxfPFSLa8LLqRauwsI" alt="Relationship img"><br>
<strong>Note:</strong><br>
All validation part depends on this foreign key relationship map.<br>
Example:<br>
If we want to create a new quest, there are two fields to be validated, <strong>quest_status_id</strong> and <strong>quest_type_id</strong>. Assuming the incoming quest_status_id is 100, however, this is no item whose <strong>quest_status_id</strong> is 100, creating is fail. And it returns a <strong>409 CONFLICT</strong> error.</p>
<h1 id="token">Token</h1>
<ul>
<li>Token system in this server is based on <a href="http://getblimp.github.io/django-rest-framework-jwt/">REST framework<br>
JWT</a>.</li>
<li>Any request with the token takes a user object to the server.</li>
<li>For more information, <a href="https://github.com/LooDaHu/ARORA_General_Introduction/blob/master/README.md">here</a>.</li>
</ul>
<h2 id="get-a-token">Get a Token</h2>
<blockquote>
<p>URL: <a href="http://127.0.0.1:8000/api-token-auth/">http://127.0.0.1:8000/api-token-auth/</a><br>
Method: POST<br>
Data in JSON: { “username”:"&lt; user_name &gt;", “password”:"&lt; password &gt;"}</p>
</blockquote>
<h2 id="verify-a-token">Verify a Token</h2>
<blockquote>
<p>URL: <a href="http://127.0.0.1:8000/api-token-verify">http://127.0.0.1:8000/api-token-verify</a><br>
Method: POST<br>
Data in JSON: { “token”:“JWT &lt; token_to_be_refresh &gt;”}</p>
</blockquote>
<h2 id="refresh-a-token">Refresh a Token</h2>
<blockquote>
<p>URL: <a href="http://127.0.0.1:8000/api-token-refresh">http://127.0.0.1:8000/api-token-refresh</a><br>
Method: POST<br>
Data in JSON: { “token”:“JWT &lt; token_to_be_refresh &gt;”}<br>
Note: ‘<a href="http://getblimp.github.io/django-rest-framework-jwt/#additional-settings">JWT_ALLOW_REFRESH</a>’ should be True to enable <a href="http://getblimp.github.io/django-rest-framework-jwt/#refresh-token">refreshing token</a>.</p>
</blockquote>
<h1 id="contact">Contact</h1>
<p>If you have any question about the above content, be free to contact me.</p>
<blockquote>
<p>Developer: Jinming Yang<br>
Email: <a href="mailto:jy345@nau.edu">jy345@nau.edu</a><br>
Github: @LooDaHu<br>
WeChat: a651120561</p>
</blockquote>
<p>And here is a simple tutorial to fast set-up about <a href="https://github.com/LooDaHu/ARORA_General_Introduction/blob/master/README.md">Django-REST-framework and Retrofit</a>.</p>

