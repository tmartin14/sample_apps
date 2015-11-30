# config.ru
require './hello'
require 'newrelic_rpm'
run Sinatra::Application
