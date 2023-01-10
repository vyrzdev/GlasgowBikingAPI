# GlasgowBikingAPI
A auto-generating historical log for nextbike availability in glasgow.
----------------------------------------------------------------------
API ROOT: https://raw.githubusercontent.com/vyrzdev/GlasgowBikingAPI/master/api
```
List Available Datasets:
  /index/info.json
  => {
    total: <count of all available>,
    most_recent: <filename here>,
    oldest: <filename here>,
    page_size: <number of datasets per page>
  }
  /index/page-<page number here>.json
  => [
    ...filenames...
  ]

  /data/<filename>
  => {
    ...stations... (which include bikes)
  }
```
