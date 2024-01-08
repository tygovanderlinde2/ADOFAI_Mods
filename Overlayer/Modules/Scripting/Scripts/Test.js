// TODO make it so that the actual time is captured instead of the CurSecond() time when a lvl starts and the level is slowed down/sped up.\

let startFlag;
let milliseconds;

On.Rewind(() => {
  startFlag = true;
});

const main = () => {
  if (startFlag) {
    startFlag = false;
    milliseconds = 0;
  }
}

// RegisterTag("test", main, true);