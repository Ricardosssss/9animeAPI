
# 9anime API

Tomorrow, I'll write the description, LOL.
## Endpoints

#### Returns some information about a given anime

```http
  GET /infos/${animeId}
```

|Parameter|Type |Description |
|:--------|:----|:-----------|
|`animeID`|`int`|**required**|


#### Returns all episodes from a given anime

```http
  GET /episodes/${animeId}
```

|Parameter|Type |Description |
|:--------|:----|:-----------|
|`animeID`|`int`|**required**|


#### Returns all animes based on your search

```http
  GET /search
```

|Parameter|Type |Description |
|:--------|:----|:-----------|
|`keyword`|`string`|**required**|
|`page`|`int`|~required~|


#### Provide the m3u8 file and some additional data about the episode

```http
  GET /watch/${episodeId}
```

|Parameter|Type |Description|
|:--------|:----|:-----------|
|`episodeId`|`int`|**required**|