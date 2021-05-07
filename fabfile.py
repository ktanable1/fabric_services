from fabric import task


SERVICES = {

  #
  # QA4
  #

  # ecomcloud  
  "webservicestomqa401.example.com" : {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-ecomcloud.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # csr
  "csrtomqa401.example.com" : {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-csr.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # estore
  "estoretomqa401.example.com": {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-estore.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # estore2
  "estoretomqa402.example.com": {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-estore.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # estore-om
  "estoreomtomqa401.example.com": {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-estore_om.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # estore-email
  "estoreemailtomqa401.example.com": {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-estore_email.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # estore-settle
  "estoresettletomqa401.example.com": {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-estore_settle.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # coherence
  "coherenceqa401.example.com": {
    "start" : """
      hostname
      cd /apps/*/coherence/
      pwd
      ls -la
      ./cache-server-start.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # searchserver master 
  "searchmastertomqa401.example.com": {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-searchmaster.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # searchserver slave
  "searchslavetomqa401.example.com": {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-searchslave.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # notifier
  "estorenotifiertomqa401.example.com": {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-notifier.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # timetravel
  "timetraveltomqa401.example.com": {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-timetravel.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # ruleengine
  "rulesenginetomqa401.example.com": {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-ruleengine.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  # cm
  "cmtomqa401.example.com": {
    "start" : """
      hostname
      cd /apps/*/deploy/deploy-script
      pwd
      ls -la
      ACTION=START sh deploy-cmserver.sh
    """,
    "stop" : """
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}')
      echo "PID: $PID"
      [[ $PID ]] && kill -9 $PID
    """,
    "status" : """
      ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy
      PID=$(ps aux | grep java | grep -v grep | grep -v sumo | grep /apps/*/deploy | awk '{print $2}' | xargs)
      echo "PID:$PID"
    """
  },

  #
  # End of QA4
  #
}



@task 
def status(c):
  try:
      print "=== host:", c.host, "==="
      c.run(SERVICES[c.host]['status'])
      print
  except:
      pass


@task 
def stop(c):
  try:
      print ">>> host:", c.host, "<<<"
      c.run(SERVICES[c.host]['stop'])
      print
  except:
      pass


@task 
def start(c):
  try:
      print "<<< host:", c.host, ">>>"  
      c.run(SERVICES[c.host]['start'])
      print
  except:
      pass

