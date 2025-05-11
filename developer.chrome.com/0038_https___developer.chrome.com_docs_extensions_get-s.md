---
url: https://developer.chrome.com/docs/extensions/get-started?hl=hi
title: https://developer.chrome.com/docs/extensions/get-started?hl=hi
date: 2025-05-11T16:52:07.119074
depth: 1
---

[ सीधे मुख्य कॉन्टेंट पर जाएं ](https://developer.chrome.com/docs/extensions/get-started?hl=hi#main-content)
  * [Español – América Latina](https://developer.chrome.com/docs/extensions/get-started?hl=es-419)




इस पेज का अनुवाद [Cloud Translation API](https://cloud.google.com/translate/?hl=hi) से किया गया है. 


###  शुरू करना 
Chrome एक्सटेंशन डेवलपमेंट में आपका स्वागत है. अपना पहला Chrome एक्सटेंशन बनाने और उसे डिस्ट्रिब्यूट करने के लिए, ज़रूरी जानकारी पाएं. 
[अपना पहला एक्सटेंशन बनाना](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world?hl=hi) [सभी ट्यूटोरियल देखना](https://developer.chrome.com/docs/extensions/get-started?hl=hi#tutorials)
###  एक्सटेंशन क्या होते हैं? 
Chrome एक्सटेंशन, यूज़र इंटरफ़ेस को पसंद के मुताबिक बनाकर, ब्राउज़र इवेंट को मॉनिटर करके, और वेब में बदलाव करके ब्राउज़िंग अनुभव को बेहतर बनाते हैं. एक्सटेंशन क्या-क्या कर सकते हैं, इसके बारे में ज़्यादा उदाहरणों के लिए [Chrome वेब स्टोर](https://chromewebstore.google.com/?hl=hi) पर जाएं. 
###  इन्हें कैसे बनाया जाता है? 
वेब ऐप्लिकेशन बनाने के लिए इस्तेमाल की जाने वाली वेब टेक्नोलॉजी का इस्तेमाल करके, एक्सटेंशन बनाए जा सकते हैं: [एचटीएमएल](https://web.dev/learn/html?hl=hi), [सीएसएस](https://web.dev/learn/css?hl=hi), और [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript). 
###  वे क्या कर सकते हैं? 
अलग-अलग काम करने के लिए, एक्सटेंशन के पास [वेब एपीआई](https://developer.mozilla.org/docs/Web/API) के साथ-साथ [Chrome एक्सटेंशन एपीआई](https://developer.chrome.com/docs/extensions/reference?hl=hi) का भी ऐक्सेस होता है. ज़्यादा जानकारी के लिए, [डेवलप करने से जुड़ी गाइड](https://developer.chrome.com/docs/extensions/develop?hl=hi) देखें. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=hi)
###  [ मेनिफ़ेस्ट ](https://developer.chrome.com/docs/extensions/reference/manifest?hl=hi)
एक्सटेंशन की मेनिफ़ेस्ट फ़ाइल ही ऐसी ज़रूरी फ़ाइल है जिसका नाम खास होना चाहिए: manifest.json. यह एक्सटेंशन की रूट डायरेक्ट्री में भी मौजूद होनी चाहिए. मेनिफ़ेस्ट, ज़रूरी मेटाडेटा रिकॉर्ड करता है, संसाधनों की जानकारी देता है, अनुमतियों की जानकारी देता है, और यह तय करता है कि कौनसी फ़ाइलों को बैकग्राउंड और पेज पर चलाना है. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=hi)
###  [ सर्विस वर्कर ](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers?hl=hi)
सर्विस वर्कर बैकग्राउंड में चलता है और ब्राउज़र इवेंट को मैनेज करता है. जैसे, बुकमार्क हटाना या टैब बंद करना. उनके पास डीओएम का ऐक्सेस नहीं होता. हालांकि, इस इस्तेमाल के उदाहरण के लिए, इसे ऑफ़स्क्रीन दस्तावेज़ के साथ जोड़ा जा सकता है. 
[ article  ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=hi)
###  [ कॉन्टेंट स्क्रिप्ट ](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts?hl=hi)
कॉन्टेंट स्क्रिप्ट, वेब पेज के कॉन्टेक्स्ट में JavaScript चलाती हैं. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=hi)
###  [ टूलबार ऐक्शन ](https://developer.chrome.com/docs/extensions/reference/api/action?hl=hi)
जब उपयोगकर्ता एक्सटेंशन टूलबार आइकॉन पर क्लिक करता है या Action API का इस्तेमाल करके कोई पॉप-अप दिखाता है, तब कोड को लागू करें. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=hi)
###  [ साइड पैनल ](https://developer.chrome.com/docs/extensions/reference/api/sidePanel?hl=hi)
ब्राउज़र के साइड पैनल में पसंद के मुताबिक यूज़र इंटरफ़ेस (यूआई) दिखाएं. 
[ article  ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=hi)
###  [ DeclarativeNetRequest ](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest?hl=hi)
नेटवर्क के अनुरोधों को इंटरसेप्ट, ब्लॉक या उनमें बदलाव करना. 
palette 
###  अच्छी क्वालिटी का एक्सटेंशन डिज़ाइन करना 
यह चुनते समय कि किन सुविधाओं के साथ काम करना है, पक्का करें कि आपका एक्सटेंशन [सिर्फ़ एक काम](https://developer.chrome.com/docs/webstore/program-policies/quality-guidelines-faq?hl=hi) करता हो. यह काम सटीक और समझने में आसान होना चाहिए. 
build 
###  नीतियों के बारे में जानना 
Chrome Web Store पर उपलब्ध कराए जाने वाले एक्सटेंशन, [डेवलपर कार्यक्रम की नीतियों](https://developer.chrome.com/docs/webstore/program-policies?hl=hi) का पालन करते हों. इन नीतियों के बारे में जानें, ताकि यह पक्का किया जा सके कि आपके एक्सटेंशन को Chrome Web Store में होस्ट किया जा सकता है. 
cloud_off 
###  एक्सटेंशन का पूरा लॉजिक शामिल करना 
कोड लिखते समय, ध्यान रखें कि सभी लॉजिक, एक्सटेंशन पैकेज में शामिल होने चाहिए. इसका मतलब है कि रनटाइम के दौरान कोई अतिरिक्त JavaScript कोड डाउनलोड नहीं किया जा सकता. [एक्सटेंशन की सुरक्षा को बेहतर बनाएं](https://developer.chrome.com/docs/extensions/migrating/improve-security?hl=hi) सेक्शन में, रिमोट तौर पर होस्ट किए गए कोड को चलाने के अन्य विकल्प मिलते हैं. 
code 
###  आपका पहला एक्सटेंशन 
अपना पहला 'नमस्ते दुनिया' एक्सटेंशन बनाएं. इससे आपको एक्सटेंशन डेवलपमेंट वर्कफ़्लो के बारे में पता चलेगा. 
code 
###  हर पेज पर स्क्रिप्ट चलाना 
किसी साइट में एलिमेंट अपने-आप जुड़ने की सुविधा सेट अप करने का तरीका जानें. 
code 
###  ऐक्टिव टैब में स्क्रिप्ट इंजेक्ट करना 
टूलबार आइकॉन पर क्लिक करके, मौजूदा पेज के स्टाइल को आसान बनाने का तरीका जानें. 
code 
###  टैब मैनेजर बनाना 
ऐसा पॉप-अप बनाने का तरीका जानें जो आपके टैब मैनेज करता है. 
code 
###  सेवा वर्कर की मदद से इवेंट मैनेज करना 
एक्सटेंशन के लिए सेवा वर्कर बनाने और उसे डीबग करने का तरीका जानें. 
code 
###  अपने एक्सटेंशन को डीबग करना 
डीबग करने के दौरान लॉग और गड़बड़ी के मैसेज ढूंढने का तरीका जानें. 

