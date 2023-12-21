function SongTime() {
  let CorrectedCurSecond;
  let CorrectedTotalSecond;
  if (CurSecond(1) < 10) {
    CorrectedCurSecond = `0${CurSecond(1)}`;
  } else {
    CorrectedCurSecond = CurSecond(1);
  }
  if (TotalSecond(1) < 10) {
    CorrectedTotalSecond = `0${TotalSecond(1)}`;
  } else {
    CorrectedTotalSecond = TotalSecond(1);
  }
  return `${CurMinute(1)}:${CorrectedCurSecond} / ${TotalMinute(1)}:${CorrectedTotalSecond}`
}
RegisterTag("SongTime", SongTime, false);