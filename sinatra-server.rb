require 'sinatra'
require 'json'

get '/' do
  'what up Chengyang'
end

get '/beers' do
  content_type :json
  {
    beers: [{
      name: "a",
        id: 1
      }, {
        name: "b",
        id: 2
      }, {
        name: "c",
        id: 3
      }, {
        name: "d",
        id: 4
      }]
  }.to_json
end
