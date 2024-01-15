function SongTime() {
  let CorrectedCurSecond;
  let CorrectedTotalSecond;
  if (CurSecondWithPitch(1) < 10) {
    CorrectedCurSecond = `0${CurSecondWithPitch(1)}`;
  } else {
    CorrectedCurSecond = CurSecondWithPitch(1);
  }
  if (TotalSecondWithPitch(1) < 10) {
    CorrectedTotalSecond = `0${TotalSecondWithPitch(1)}`;
  } else {
    CorrectedTotalSecond = TotalSecondWithPitch(1);
  }
  return `${CurMinuteWithPitch
    (1)}:${CorrectedCurSecond} / ${TotalMinuteWithPitch(1)}:${CorrectedTotalSecond}`
}
RegisterTag("SongTime", SongTime, false);