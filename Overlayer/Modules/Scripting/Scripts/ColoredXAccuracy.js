function CXAccuracy() {
  if (XAccuracy(10) <= 90) return ('<color=#FF0000>' + XAccuracy(10) + '%' + '</color>')
  if (XAccuracy(10) > 90 && XAccuracy(10) < 99) return ('<color=#FFD580>' + XAccuracy(10) + '%' + '</color>')
  if (XAccuracy(10) >= 99) return ('<color=#00FF00>' + XAccuracy(10) + '%' + '</color>')
  return ('<color=#00FF00>' + 100 + '%' + '</color>')
}
RegisterTag("CXAccuracy", CXAccuracy, false);