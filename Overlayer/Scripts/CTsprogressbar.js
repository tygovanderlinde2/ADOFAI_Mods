function CTprogressbar() {
    const line = 2480 * (CurMinute() * 60000 + CurSecond() * 1000 + CurMilliSecond()) / (TotalMinute() * 60000 + TotalSecond() * 1000 + TotalMilliSecond());
    let stick = "";

    stick += "<cspace=-0.440xem>";
    for (let i = 1; i <= Math.floor(line / 40); i++) { stick += "█"; }

    stick += "<cspace=-0.742em>";
    for (let i = 1; i <= line % 40; i++) { stick += "▏"; }
    stick += "</cspace>";
    stick += "</cspace>";
    return stick;
}

RegisterTag("CTprogressbar", CTprogressbar, true);