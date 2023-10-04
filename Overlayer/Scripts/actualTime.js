function aTime() {
  let totalSeconds = (TotalMinute(1) * 60) + TotalSecond(1);
  let actualTimeMinutes = Math.floor((totalSeconds / EditorPitch(2)) / 60, 1);
  let actualTimeSeconds = Math.floor((totalSeconds / EditorPitch(2)) % 60, 1);
  if (EditorPitch(2) === 1.00) return;
  return `${actualTimeMinutes}:${actualTimeSeconds}`;
}
RegisterTag("aTime", aTime, false);