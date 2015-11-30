# hello.rb
require 'sinatra'

get '/' do
    code = "<h1>Hello World!</h1>  <br/>This is a <b>Ruby</b> app running on Cloud Foundry.<br/><br/><br/><b>Time:</b> <%= Time.now %>"
    erb code
end
