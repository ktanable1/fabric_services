#!/bin/sh

USERNAME="tomcat"
QA4_ECOM="${USERNAME}@webservicestomqa4.example.com"
QA4_CSR="${USERNAME}@csrtomqa4.example.com"
QA4_ESTORE1="${USERNAME}@estoretomqa4.example.com"
QA4_ESTORE2="${USERNAME}@estoretomqa4.example.com"
QA4_ESTORE_EMAIL="${USERNAME}@estoreemailtomqa4.example.com"
QA4_ESTORE_OM="${USERNAME}@estoreomtomqa4.example.com"
QA4_ESTORE_SETTLE="${USERNAME}@estoresettletomqa4.example.com"
QA4_COHERENCE="${USERNAME}@coherenceqa4.example.com"
QA4_SEARCHSERVER_MASTER="${USERNAME}@searchmastertomqa4.example.com"
QA4_SEARCHSERVER_SLAVE="${USERNAME}@searchslavetomqa4.example.com"
QA4_NOTIFIER="${USERNAME}@estorenotifiertomqa4.example.com"
QA4_TIMETRAVEL="${USERNAME}@timetraveltomqa4.example.com"
QA4_SYMRULEENGINE="${USERNAME}@rulesenginetomqa4.example.com"
QA4_CM="${USERNAME}@cmtomqa4.example.com"


export COHERENCE_CLUSTER="$QA4_ECOM,$QA4_CSR,$QA4_ESTORE1,$QA4_ESTORE2,$QA4_ESTORE_EMAIL,$QA4_ESTORE_OM,$QA4_ESTORE_SETTLE,$QA4_COHERENCE"
export COHERENCE_CLUSTER_STOP_SEQ=$COHERENCE_CLUSTER
export COHERENCE_CLUSTER_START_SEQ="$QA4_COHERENCE,$QA4_ECOM,$QA4_CSR,$QA4_ESTORE1,$QA4_ESTORE2,$QA4_ESTORE_EMAIL,$QA4_ESTORE_OM,$QA4_ESTORE_SETTLE"

export SEARCH_CLUSTER="$QA4_SEARCHSERVER_MASTER,$QA4_SEARCHSERVER_SLAVE"
export SEARCH_CLUSTER_STOP_SEQ=$SEARCH_CLUSTER
export SEARCH_CLUSTER_START_SEQ=$SEARCH_CLUSTER

export REST="$QA4_NOTIFIER,$QA4_TIMETRAVEL,$QA4_SYMRULEENGINE,$QA4_CM"


#
# Groups
#

# whole cluster
qa4_start_all() {
  fab -H $COHERENCE_CLUSTER_STOP_SEQ,$SEARCH_CLUSTER_STOP_SEQ,$REST   stop
  fab -H $COHERENCE_CLUSTER_START_SEQ,$SEARCH_CLUSTER_START_SEQ,$REST start
}

qa4_stop_all() {
  fab -H $COHERENCE_CLUSTER_STOP_SEQ,$SEARCH_CLUSTER_STOP_SEQ,$REST stop
}

qa4_status_all() {
  fab -H $COHERENCE_CLUSTER,$SEARCH_CLUSTER,$REST status
}


# coherence cluster
qa4_start_coherence_cluster() {
  fab -H $COHERENCE_CLUSTER_STOP_SEQ   stop
  fab -H $COHERENCE_CLUSTER_START_SEQ  start
}

qa4_stop_coherence_cluster() {
  fab -H $COHERENCE_CLUSTER_STOP_SEQ  stop
}

qa4_status_coherence_cluster() {
  fab -H $COHERENCE_CLUSTER  status
}

# searchservers
qa4_start_searchserver_cluster() {
  fab -H $SEARCH_CLUSTER_STOP_SEQ   stop
  fab -H $SEARCH_CLUSTER_START_SEQ  start
}

qa4_stop_searchserver_cluster() {
  fab -H $SEARCH_CLUSTER_STOP_SEQ  stop
}

qa4_status_searchserver_cluster() {
  fab -H $SEARCH_CLUSTER  status
}

# rest
qa4_start_rest() {
  fab -H $REST  stop
  fab -H $REST  start
}

qa4_stop_rest() {
  fab -H $REST  stop
}

qa4_status_rest() {
  fab -H $REST  status
}


#
# Individual
#

# coherence
qa4_start_coherence() {
  fab -H $QA4_COHERENCE stop
  fab -H $QA4_COHERENCE start
}

qa4_stop_coherence() {
  fab -H $QA4_COHERENCE stop
}

qa4_status_coherence() {
  fab -H $QA4_COHERENCE status
}

# ecomcloud
qa4_start_ecomcloud() {
  fab -H $QA4_ECOM stop
  fab -H $QA4_ECOM start
}

qa4_stop_ecomcloud() {
  fab -H $QA4_ECOM stop
}

qa4_status_ecomcloud() {
  fab -H $QA4_ECOM status
}

# csr
qa4_start_csr() {
  fab -H $QA4_CSR stop
  fab -H $QA4_CSR start
}

qa4_stop_csr() {
  fab -H $QA4_CSR stop
}

qa4_status_csr() {
  fab -H $QA4_CSR status
}

# estore
qa4_start_estore() {
  fab -H $QA4_ESTORE1 stop
  fab -H $QA4_ESTORE1 start
}

qa4_stop_estore() {
  fab -H $QA4_ESTORE1 stop
}

qa4_status_estore() {
  fab -H $QA4_ESTORE1 status
}

# estore2
qa4_start_estore2() {
  fab -H $QA4_ESTORE2 stop
  fab -H $QA4_ESTORE2 start
}

qa4_stop_estore2() {
  fab -H $QA4_ESTORE2 stop
}

qa4_status_estore2() {
  fab -H $QA4_ESTORE2 status
}

# estore-om
qa4_start_estore_om() {
  fab -H $QA4_ESTORE_OM stop
  fab -H $QA4_ESTORE_OM start
}

qa4_stop_estore_om() {
  fab -H $QA4_ESTORE_OM stop
}

qa4_status_estore_om() {
  fab -H $QA4_ESTORE_OM status
}

# estore-email
qa4_start_estore_email() {
  fab -H $QA4_ESTORE_EMAIL stop
  fab -H $QA4_ESTORE_EMAIL start
}

qa4_stop_estore_email() {
  fab -H $QA4_ESTORE_EMAIL stop
}

qa4_status_estore_email() {
  fab -H $QA4_ESTORE_EMAIL status
}

# estore-settle
qa4_start_estore_settle() {
  fab -H $QA4_ESTORE_SETTLE stop
  fab -H $QA4_ESTORE_SETTLE start
}

qa4_stop_estore_settle() {
  fab -H $QA4_ESTORE_SETTLE stop
}

qa4_status_estore_settle() {
  fab -H $QA4_ESTORE_SETTLE status
}

# searchserver master
qa4_start_searchserver_master() {
  fab -H $QA4_SEARCHSERVER_MASTER stop
  fab -H $QA4_SEARCHSERVER_MASTER start
}

qa4_stop_searchserver_master() {
  fab -H $QA4_SEARCHSERVER_MASTER stop
}

qa4_status_searchserver_master() {
  fab -H $QA4_SEARCHSERVER_MASTER status
}

# searchserver slave
qa4_start_searchserver_slave() {
  fab -H $QA4_SEARCHSERVER_SLAVE stop
  fab -H $QA4_SEARCHSERVER_SLAVE start
}

qa4_stop_searchserver_slave() {
  fab -H $QA4_SEARCHSERVER_SLAVE stop
}

qa4_status_searchserver_slave() {
  fab -H $QA4_SEARCHSERVER_SLAVE status
}

# notifier
qa4_start_notifier() {
  fab -H $QA4_NOTIFIER stop
  fab -H $QA4_NOTIFIER start
}

qa4_stop_notifier() {
  fab -H $QA4_NOTIFIER stop
}

qa4_status_notifier() {
  fab -H $QA4_NOTIFIER status
}

# timetravel
qa4_start_timetravel() {
  fab -H $QA4_TIMETRAVEL stop
  fab -H $QA4_TIMETRAVEL start
}

qa4_stop_timetravel() {
  fab -H $QA4_TIMETRAVEL stop
}

qa4_status_timetravel() {
  fab -H $QA4_TIMETRAVEL status
}

# symruleengine
qa4_start_symruleengine() {
  fab -H $QA4_SYMRULEENGINE stop
  fab -H $QA4_SYMRULEENGINE start
}

qa4_stop_symruleengine() {
  fab -H $QA4_SYMRULEENGINE stop
}

qa4_status_symruleengine() {
  fab -H $QA4_SYMRULEENGINE status
}

# cm
qa4_start_cm() {
  fab -H $QA4_CM stop
  fab -H $QA4_CM start
}

qa4_stop_cm() {
  fab -H $QA4_CM stop
}

qa4_status_cm() {
  fab -H $QA4_CM status
}
