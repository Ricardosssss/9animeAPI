
# 9anime API

Tomorrow, I'll write the description, LOL.
## Endpoints

#### Returns some information about a given anime

```
  GET /infos/${animeId}
```

|Parameter|Type |Description |
|:--------|:----|:-----------|
|`animeID`|`int`|**required**|


#### Returns all episodes from a given anime

```
  GET /episodes/${animeId}
```

|Parameter|Type |Description |
|:--------|:----|:-----------|
|`animeID`|`int`|**required**|


#### Returns all animes based on your search

```
  GET /search
```

|Parameter|Type |Description |
|:--------|:----|:-----------|
|`keyword`|`string`|**required**|
|`page`|`int`|~required~|


#### Provide the m3u8 file and some additional data about the episode

```
  GET /watch/${episodeId}
```

|Parameter|Type |Description|
|:--------|:----|:-----------|
|`episodeId`|`int`|**required**|