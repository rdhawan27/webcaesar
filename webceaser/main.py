#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

def input_text(texttoencode):
    Header= "<h2> Ceaser web </h2>"
    rot_label= "<label> Rotation number:  </label>"
    rotation_number = "<input type='number' name='rot_number'/>"

    text_to_encode="<label> Please input the label to encode:  </label>"
    textarea= "<textarea name='message'>" + texttoencode + "</textarea>"

    submit= "<input type = 'submit'/>"


    form= ("<form method='post'>"
        + Header
        + rot_label + rotation_number +"<br>"+"<br>"
        + text_to_encode + textarea +"<br>" + "<br>"
        + submit
        +"</form>")

    return form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content=input_text(" ")
        self.response.write(content)

    def post(self):
        message=self.request.get("message")
        rotation_number=(self.request.get("rot_number"))
        rotation_number=int(rotation_number)
        encrypt_message=caesar.encrypt(message,rotation_number)
        escaped_message=cgi.escape(encrypt_message)
        content=input_text(escaped_message)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
