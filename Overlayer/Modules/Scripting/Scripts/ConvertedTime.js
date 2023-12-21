function ConvertedTime() {
  let ConvertedMinute = Minute();
  let ConvertedSecond = Second();
  if (Minute() < 10) {
    ConvertedMinute = `0${Minute()}`
  }
  if (Second() < 10) {
    ConvertedSecond = `0${Second()}`
  }
  return `${Hour()}:${ConvertedMinute}:${ConvertedSecond}`
}
RegisterTag("ConvertedTime", ConvertedTime, false);