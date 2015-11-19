var mClient;
var mTopic="topic-15-1119A/device-1/matrix-1";

onload = function() {
	var clientId = "clientid-15-1119P-12345";
//    mClient = new Paho.MQTT.Client("test.mosquitto.org", 8080, "/", clientId);
    mClient = new Paho.MQTT.Client("192.168.10.1", 8080, "/", clientId);

	mClient.connect({
	  onSuccess:function(){
	    console.log("con_success");
	  }
	  , onFailure:function(){console.log("con_fail")}
	});
	document.querySelector('#id-a-on').onclick = function() {
		var msg=$('input#id-text').val();
		publish_relay( msg );
	};
}
//
function publish_relay(value){
    message = new Paho.MQTT.Message(value);
    message.destinationName = mTopic;
    mClient.send(message);
};	

