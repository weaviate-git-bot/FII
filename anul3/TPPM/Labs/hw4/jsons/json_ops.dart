import 'dart:io';
import 'dart:convert';

Map<String, dynamic> jsonSubJson(String jsonPath1, String jsonPath2) {
  var firstJson = jsonDecode(File(jsonPath1).readAsStringSync());
  var secondJson = jsonDecode(File(jsonPath2).readAsStringSync());

  var result = <String, dynamic>{};

  for (var i in firstJson.keys) {
    if (!secondJson.containsKey(i)) {
      result[i] = firstJson[i];
    }
  }

  for (var i in secondJson.keys) {
    if (!firstJson.containsKey(i)) {
      result[i] = secondJson[i];
    }
  }

  return result;
}
