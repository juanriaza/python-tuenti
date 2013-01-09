## API SPEC

### Methods

* [`AppUpdate_checkUpdate`](#appupdate_checkupdate)
* [`Auth_closeSession`](#auth_closesession)
* [`Auth_getSessionInfo`](#auth_getsessioninfo)
* [`Block_blockUsers`](#block_blockusers)
* [`Block_getBlockedUsers`](#block_getblockedusers)
* [`Block_unblockUsers`](#block_unblockusers)
* [`Chat_getChatUnreadCounts`](#chat_getchatunreadcounts)
* [`Chat_getLatestChatMessagesInConversation`](#chat_getlatestchatmessagesinconversation)
* [`Chat_uploadPhoto`](#chat_uploadphoto)
* [`Feed_getCurrentShare`](#feed_getcurrentshare)
* [`Feed_getProfileFeedByTime`](#feed_getprofilefeedbytime)
* [`Feed_getShareFeed`](#feed_getsharefeed)
* [`Feed_getSharedEvent`](#feed_getsharedevent)
* [`Feed_updateEventCountersByTime`](#feed_updateeventcountersbytime)
* [`FriendRequest_acceptFriendRequests`](#friendrequest_acceptfriendrequests)
* [`FriendRequest_addContacts`](#friendrequest_addcontacts)
* [`FriendRequest_cancelFriendRequests`](#friendrequest_cancelfriendrequests)
* [`FriendRequest_downgradeFriendsToContacts`](#friendrequest_downgradefriendstocontacts)
* [`FriendRequest_ignoreFriendRequests`](#friendrequest_ignorefriendrequests)
* [`FriendRequest_sendFriendRequests`](#friendrequest_sendfriendrequests)
* [`Importer_checkPhoneBookDifferences`](#importer_checkphonebookdifferences)
* [`Importer_findUserByEmail`](#importer_finduserbyemail)
* [`Importer_findUserByPhone`](#importer_finduserbyphone)
* [`Importer_getInviteToMessengerList`](#importer_getinvitetomessengerlist)
* [`Importer_getPhoneBookState`](#importer_getphonebookstate)
* [`Importer_setPhoneBookSignature`](#importer_setphonebooksignature)
* [`Importer_syncMessengerUserList`](#importer_syncmessengeruserlist)
* [`Importer_updateContacts`](#importer_updatecontacts)
* [`Notification_getContentReactions`](#notification_getcontentreactions)
* [`Notification_getCounts`](#notification_getcounts)
* [`Notification_getNewPeople`](#notification_getnewpeople)
* [`Notification_markContentReactionsAsSeen`](#notification_markcontentreactionsasseen)
* [`Notification_markNewPeopleAsSeen`](#notification_marknewpeopleasseen)
* [`Profile_getAlbumPhotos`](#profile_getalbumphotos)
* [`Profile_getProfileInfo`](#profile_getprofileinfo)
* [`Push_subscribeToPush`](#push_subscribetopush)
* [`Push_unsubscribeFromPush`](#push_unsubscribefrompush)
* [`Registration_challengePhoneNumber`](#registration_challengephonenumber)
* [`Registration_createNewAccount`](#registration_createnewaccount)
* [`Registration_getAvailableCountryCodes`](#registration_getavailablecountrycodes)
* [`Registration_sendRecoverPasswordEmail`](#registration_sendrecoverpasswordemail)
* [`Registration_verifyPhoneNumber`](#registration_verifyphonenumber)
* [`Settings_open`](#settings_open)
* [`Share_dislike`](#share_dislike)
* [`Share_getComments`](#share_getcomments)
* [`Share_getLikers`](#share_getlikers)
* [`Share_like`](#share_like)
* [`Share_postComment`](#share_postcomment)
* [`Share_postShareEvent`](#share_postshareevent)
* [`Share_setUserAvatar`](#share_setuseravatar)
* [`User_getRelationshipData`](#user_getrelationshipdata)
* [`User_getUsersData`](#user_getusersdata)
* [`User_updateRelationshipData`](#user_updaterelationshipdata)

----

### `AppUpdate_checkUpdate`

#### Params

- `userAgent`
	- Type: String 
- `version`
	- Type: String	

----
	
### `Auth_closeSession`

#### Params

- `installationId`
	- Type: String
	
----

### `Auth_getSessionInfo`

#### Params

- `installationId`
	- Type: String

----

### `Block_blockUsers`

#### Params

- `ids`
	- Type: List[String]

----

### `Block_getBlockedUsers`

----

### `Block_unblockUsers`

#### Params

- `ids`
	- Type: List[String]

----

### `Chat_getChatUnreadCounts`

#### Params

- `includeOpen`
	- Type: boolean
	- Optional

----

### `Chat_getLatestChatMessagesInConversation`

#### Params

- `conversationId`
	- Type: String
- `limit`
	- Type: int
- `xmppTimestamp`
	- Type: String
- `allPending`
	- Type: boolean

----

### `Chat_uploadPhoto`

#### Params

- `conversationId`
	- Type: String

----

### `Feed_getCurrentShare`

----

### `Feed_getProfileFeedByTime`

#### Params

- `userId`
	- Type: String
- `before`
	- Type: long
- `max`
	- Type: int

----

### `Feed_getShareFeed`

#### Params

- `max`
	- Type: String
	- Value: 20
- `after`
	- Type: long
	- Optional
	- Value: -1L

----

### `Feed_getSharedEvent`

#### Params

- `shareId`
	- Type: String

----

### `Feed_updateEventCountersByTime`

#### Params

- `ranges`
	- Type: List[List[long]]
	
----

### `FriendRequest_acceptFriendRequests`

#### Params

- `ids`
	- Type: List[String]
	
----

### `FriendRequest_addContacts`

#### Params

- `ids`
	- Type: List[String]
	
----

### `FriendRequest_cancelFriendRequests`

#### Params

- `ids`
	- Type: List[String]
	
----

### `FriendRequest_downgradeFriendsToContacts`

#### Params

- `ids`
	- Type: List[String]

----

### `FriendRequest_ignoreFriendRequests`

#### Params

- `ids`
	- Type: List[String]

----

### `FriendRequest_sendFriendRequests`

#### Params

- `ids`
	- Type: List[String]

----

### `Importer_checkPhoneBookDifferences`

#### Params

- `installationId`
	- Type: String
- `contactSignatures`
	- Structure: List[{'luid': String, 'signature': String}]
- `chunkOffset`
	- Type: int 
- `numChunks`
	- Type: int

----

### `Importer_findUserByEmail`

#### Params

- `email`
	- Type: String

----

### `Importer_findUserByPhone`

#### Params

- `msisdn`
	- Type: String
	
----

### `Importer_getInviteToMessengerList`

#### Params

- `installationId`
	- Type: String

----

### `Importer_getPhoneBookState`

#### Params

- `installationId`
	- Type: String
- `signature`
	- Type: String

----

### `Importer_setPhoneBookSignature`

#### Params

- `installationId`
	- Type: String
- `signature`
	- Type: String

----

### `Importer_syncMessengerUserList`

#### Params

- `installationId`
	- Type: String
- `returnAdded`
	- Type: boolean
- `explicit`
	- Type: boolean
	
----

### `Importer_updateContacts`

#### Params

- `installationId`
	- Type: String
- `contacts`
	- Structure:
	```python
	[{'data': {
		'phones': [{'number': String, 'label': String, 'type': String}],
	    'emails': [{'mail': String, 'label': String, 'type': String}]},
	    	'name': String,
	    	'surname': String,
	    	'fullnameNormalized': String,
	    	'avatarUri': Uri,
	    	'version': long,
	    	'id': long}]
	```
- `deviceInfo`
	- Structure: {'name': String, 'make': String, 'model': String}

Notes:

- `contacts`
	- TODO
- `deviceInfo`
	- 'name' = android.os.Build.PRODUCT
	- 'make' = android.os.Build.MANUFACTURER
	- 'model' = android.os.Build.MODEL

----

### `Notification_getContentReactions`

#### Params

- `markAsSeen`
	- Type: boolean

----

### `Notification_getCounts`
	
----

### `Notification_getNewPeople`

#### Params

- `markAsSeen`
	- Type: boolean
	
----

### `Notification_markContentReactionsAsSeen`

#### Params

- `timestamp`
	- Type: long

----

### `Notification_markNewPeopleAsSeen`

#### Params

- `timestamp`
	- Type: long
	
----
	
### `Profile_getAlbumPhotos`

#### Params

- `userId`
	- Type: String
- `page`
	- Type: int
- `pageSize`
	- Type: int

----

### `Profile_getProfileInfo`

#### Params

- `userId`
	- Type: String
	
----

### `Push_subscribeToPush`

#### Params

- `pushToken`
	- Type: String
- `installationId`
	- Type: String

----

### `Push_unsubscribeFromPush`

#### Params

- `installationId`
	- Type: String

----

### `Registration_challengePhoneNumber`

#### Params

- `msisdn`
	- Type: String

----

### `Registration_createNewAccount`

#### Params

- `email`
	- Type: String
- `name`
	- Type: String
- `last`
	- Type: String
- `gender`
	- Type: int
- `installationId`
	- Type: String
- `deviceFamily`
	- Type: String

----

### `Registration_getAvailableCountryCodes`

----

### `Registration_sendRecoverPasswordEmail`

#### Params

- `email`
	- Type: String

----

### `Registration_verifyPhoneNumber`

#### Params

- `msisdn`
	- Type: String
- `handshake`
	- Type: String
- `timestamp`
	- Type: long
- `seed`
	- Type: String

----

### `Settings_open`

#### Params

- `deviceFamily`
	- Type: String
	- Value: 'MDI3MDFmZjU4MGExNWM0YmEyYjA5MzRkODlmMjg0MTU6MC4yMjk5ODcwMCAxMzI0NDg5NjY0'
- `installationId`
	- Type: String
- `userAgent`
	- Type: String
- `version`
	- Type: String

----

### `Share_dislike`

#### Params

- `shareId`
	- Type: String

----

### `Share_getComments`

#### Params

- `shareId`
	- Type: String
- `page`
	- Type: int
- `pageSize`
	- Type: int

----

### `Share_getLikers`

#### Params

- `shareId`
	- Type: String
- `page`
	- Type: int
- `pageSize`
	- Type: int

----

### `Share_like`

#### Params

- `shareId`
	- Type: String

----

### `Share_postComment`

#### Params

- `shareId`
	- Type: String
- `body`
	- Type: String

----

### `Share_postShareEvent`

#### Params

- `body`
	- Type: String
- `photoKey`
	- Type: String

----

### `Share_setUserAvatar`

#### Params

- `x`
	- Type: int
- `y`
	- Type: int

----

### `User_getRelationshipData`

#### Params

- `relationship`
	- Type: String
- `page`
	- Type: int
- `pageSize`
	- Type: int

----

### `User_getUsersData`

#### Params

- `ids`
	- Type: List[String]

----

### `User_updateRelationshipData`

#### Params

- `friends`
	- Type: List[String]
- `contacts`
	- Type: List[String]
- `weak`
	- Type: List[String]
- `timestamp`
	- Type: long

