<h3 id="exercise-01-screwdriver-song">Exercise 00: Screwdriver Song</h3>

 &mdash; So, what about that over device? Some kinda screwdriver, eh?

 &mdash; Sonic, yes.

 &mdash; What can it do? Can I get one?

 &mdash; Well, it generates a combination of certain frequencies, so you can do...pretty much
 anything!

 &mdash; Can it actually unscrew stuff?

 &mdash; Oh, it's kinda tricky. To do that... you know what, here, just play these sound files.

---

This time you need to create a simple WSGI+HTTP client-server application for managing sound files.

First, the server. It shouldn't use any kind of database, just storing files on disk is okay. Web
interface should run on port 8888. When opened, the webpage should show a list of sound files
already uploaded as well as the button for uploading one more. As a user, you should be able to
click on that button, upload the file to the server and it should appear in a list of files shown
on the webpage.

Also, the server should perform a [MIME type](https://en.wikipedia.org/wiki/Media_type) check, so
only audio files are accepted (e.g. `mp3`, `ogg` and `wav`). If a non-audio file is uploaded (e.g.
`jpg`, `exe` or `docx`), it should be discarded and the webpage should show the message "Non-audio
file detected". 

For some bonus points, you can implement playing uploaded sound files directly from the webpage.

This time you are not limited to built-in WSGI server, so it is recommended to use either [Flask](https://flask.palletsprojects.com/)
or [Django](https://www.djangoproject.com/) framework for this task, even though it is not a strict
requirement. Don't forget to add any third-party dependencies you've used into file
`requirements.txt`. Please also include file `README` explaining how to start the HTTP server
(it should contain the specific command to run).

Second, the client. It should be a command-line application with two possible actions:

- `python screwdriver.py upload /path/to/file.mp3` should upload the local audio file
  `/path/to/file.mp3` to the server
- `python screwdriver.py list` should retrieve and print out the names of all the files currently
  present on the server.

All the client-server intercommunication should be using HTTP. It is recommended (though not
strictly required) to use either [Requests](https://docs.python-requests.org/en/latest/) or [HTTPX](https://www.python-httpx.org/) library for
performing HTTP queries.