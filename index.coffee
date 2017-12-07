command: "python3 ./reddit-overview.widget/script.py"

## edit to your liking!
settings: {
  columns: 2,
}
refreshFrequency: 60000

style: """
  bottom: 90px
  left: 15px
  font-size: 30px
  font-family: Helvetica Neue
  font-weight: 200
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  color: #fff

  td 
    padding: 5px

  img
    height: 36px
    width: 36px
    vertical-align: middle

  .redditor img
    border-radius: 4px

  .subreddit img
    border-radius: 50%
"""

render: (_) -> "<table><tr><td>Loading...</td></tr></table>"

afterRender: (domEl) ->
  $(domEl).on 'click', '.redditor', (e) =>
    redditor = $(e.currentTarget).attr 'data-redditor'
    @run "open https://www.reddit.com/u/" + redditor

  $(domEl).on 'click', '.subreddit', (e) =>
    subreddit = $(e.currentTarget).attr 'data-subreddit'
    @run "open https://www.reddit.com/r/" + subreddit

renderUser: (redditor, redditordata) ->
  """
  <td>
    <div class='redditor' data-redditor='#{redditor}'>
      <img style='background-color: #{redditordata["key_color"]}' src='#{redditordata["image"]}'>
      <span>#{redditordata["karma"]}</span>
    </div>
  </td>
  """

renderSub: (subreddit, subdata) ->
  """
  <td>
    <div class='subreddit' data-subreddit='#{subreddit}'>
      <img style='background-color: #{subdata["key_color"]}' src='#{subdata["image"]}'>
      <span>r/#{subreddit}</span>
    </div>
  </td>
  """

renderer: (table, data, func) ->
  i = @settings.columns
  for key, value of data
    if !(i % @settings.columns)
      table.append "<tr/>"
    i++
    table.find("tr:last").append func(key, value)

update: (output, domEl) ->
  try
    data = JSON.parse(output)
  catch e
    return

  table = $(domEl).find('table')
  table.html ""

  if data['error']
    table.html data['error']
  else
    @renderer table, data['users'], @renderUser
    @renderer table, data['subs'],  @renderSub
