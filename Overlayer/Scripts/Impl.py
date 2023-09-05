def PlayPoint(digits:int) -> float: return PlayPoint(digits)
def LevelId() -> str: return LevelId()
def IntegratedDifficulty(arg:int) -> float: return IntegratedDifficulty(arg)
def ForumDifficulty(arg:int) -> float: return ForumDifficulty(arg)
def PredictedDifficulty(arg:int) -> float: return PredictedDifficulty(arg)
def CurHit() -> str: return CurHit()
def CurTE() -> str: return CurTE()
def CurVE() -> str: return CurVE()
def CurEP() -> str: return CurEP()
def CurP() -> str: return CurP()
def CurLP() -> str: return CurLP()
def CurVL() -> str: return CurVL()
def CurTL() -> str: return CurTL()
def CurDifficulty() -> str: return CurDifficulty()
def Combo() -> str: return Combo()
def MissCount() -> str: return MissCount()
def Overloads() -> str: return Overloads()
def Expression(expr:str) -> object: return Expression(expr)
def TEHex() -> str: return TEHex()
def VEHex() -> str: return VEHex()
def EPHex() -> str: return EPHex()
def PHex() -> str: return PHex()
def LPHex() -> str: return LPHex()
def VLHex() -> str: return VLHex()
def TLHex() -> str: return TLHex()
def MPHex() -> str: return MPHex()
def FMHex() -> str: return FMHex()
def FOHex() -> str: return FOHex()
def LHit() -> str: return LHit()
def LTE() -> str: return LTE()
def LVE() -> str: return LVE()
def LEP() -> str: return LEP()
def LP() -> str: return LP()
def LLP() -> str: return LLP()
def LVL() -> str: return LVL()
def LTL() -> str: return LTL()
def Radius(digits:int) -> float: return Radius(digits)
def Pitch(digits:int) -> float: return Pitch(digits)
def EditorPitch(digits:int) -> float: return EditorPitch(digits)
def ShortcutPitch(digits:int) -> float: return ShortcutPitch(digits)
def Title() -> str: return Title()
def Author() -> str: return Author()
def Artist() -> str: return Artist()
def TitleRaw() -> str: return TitleRaw()
def AuthorRaw() -> str: return AuthorRaw()
def ArtistRaw() -> str: return ArtistRaw()
def Accuracy(digits:int) -> float: return Accuracy(digits)
def Progress(digits:int) -> float: return Progress(digits)
def CheckPoint() -> str: return CheckPoint()
def TotalCheckPoint() -> str: return TotalCheckPoint()
def XAccuracy(digits:int) -> float: return XAccuracy(digits)
def Year() -> str: return Year()
def Month() -> str: return Month()
def Day() -> str: return Day()
def Hour() -> str: return Hour()
def Minute() -> str: return Minute()
def Second() -> str: return Second()
def MilliSecond() -> str: return MilliSecond()
def DifficultyStr() -> str: return DifficultyStr()
def NHit() -> str: return NHit()
def NTE() -> str: return NTE()
def NVE() -> str: return NVE()
def NEP() -> str: return NEP()
def NP() -> str: return NP()
def NLP() -> str: return NLP()
def NVL() -> str: return NVL()
def NTL() -> str: return NTL()
def ProgressDeath(opt:str) -> float: return ProgressDeath(opt)
def SHit() -> str: return SHit()
def STE() -> str: return STE()
def SVE() -> str: return SVE()
def SEP() -> str: return SEP()
def SP() -> str: return SP()
def SLP() -> str: return SLP()
def SVL() -> str: return SVL()
def STL() -> str: return STL()
def LScore() -> str: return LScore()
def NScore() -> str: return NScore()
def SScore() -> str: return SScore()
def Score() -> str: return Score()
def Timing(arg:int) -> float: return Timing(arg)
def Attempts() -> str: return Attempts()
def FailCount() -> str: return FailCount()
def StartProgress(arg:int) -> float: return StartProgress(arg)
def BestProgress(arg:int) -> float: return BestProgress(arg)
def CurMinute() -> str: return CurMinute()
def CurSecond() -> str: return CurSecond()
def CurMilliSecond() -> str: return CurMilliSecond()
def TotalMinute() -> str: return TotalMinute()
def TotalSecond() -> str: return TotalSecond()
def TotalMilliSecond() -> str: return TotalMilliSecond()
def CurCheckPoint() -> str: return CurCheckPoint()
def StartTile() -> str: return StartTile()
def LeftTile() -> str: return LeftTile()
def CurTile() -> str: return CurTile()
def TotalTile() -> str: return TotalTile()
def TileBpm(arg:int) -> float: return TileBpm(arg)
def CurBpm(arg:int) -> float: return CurBpm(arg)
def RecKPS(arg:int) -> float: return RecKPS(arg)
def FrameTime(arg:int) -> float: return FrameTime(arg)
def Fps(arg:int) -> float: return Fps(arg)
def Multipress() -> str: return Multipress()
def TimingAvg(digits:float) -> float: return TimingAvg(digits)
def PlayTime(opt:str) -> float: return PlayTime(opt)
class Color():
  def __init__(self):
    self.r:float = None
    self.g:float = None
    self.b:float = None
    self.a:float = None
  def Equals(self, obj:object) -> bool: return self.Equals(obj)
  def GetHashCode(self) -> int: return self.GetHashCode()
  def ToString(self) -> str: return self.ToString()
class GradientColor():
  def __init__(self):
    self.topLeft:Color = None
    self.topRight:Color = None
    self.bottomLeft:Color = None
    self.bottomRight:Color = None
  def Equals(self, obj:object) -> bool: return self.Equals(obj)
  def GetHashCode(self) -> int: return self.GetHashCode()
  def ToString(self) -> str: return self.ToString()
class Vector2():
  def __init__(self):
    self.x:float = None
    self.y:float = None
    self.Item:float = None
    self.normalized:"Vector2" = None
    self.magnitude:float = None
    self.sqrMagnitude:float = None
    kEpsilon:float = None
    kEpsilonNormalSqrt:float = None
    zero:"Vector2" = None
    one:"Vector2" = None
    up:"Vector2" = None
    down:"Vector2" = None
    left:"Vector2" = None
    right:"Vector2" = None
    positiveInfinity:"Vector2" = None
    negativeInfinity:"Vector2" = None
  @staticmethod
  def Angle(_from:"Vector2", to:"Vector2") -> float: return Vector2.Angle(_from, to)
  @staticmethod
  def ClampMagnitude(vector:"Vector2", maxLength:float) -> "Vector2": return Vector2.ClampMagnitude(vector, maxLength)
  @staticmethod
  def Distance(a:"Vector2", b:"Vector2") -> float: return Vector2.Distance(a, b)
  @staticmethod
  def Dot(lhs:"Vector2", rhs:"Vector2") -> float: return Vector2.Dot(lhs, rhs)
  def Equals(self, other:object) -> bool: return self.Equals(other)
  def Equals(self, other:"Vector2") -> bool: return self.Equals(other)
  def GetHashCode(self) -> int: return self.GetHashCode()
  @staticmethod
  def Lerp(a:"Vector2", b:"Vector2", t:float) -> "Vector2": return Vector2.Lerp(a, b, t)
  @staticmethod
  def LerpUnclamped(a:"Vector2", b:"Vector2", t:float) -> "Vector2": return Vector2.LerpUnclamped(a, b, t)
  @staticmethod
  def Max(lhs:"Vector2", rhs:"Vector2") -> "Vector2": return Vector2.Max(lhs, rhs)
  @staticmethod
  def Min(lhs:"Vector2", rhs:"Vector2") -> "Vector2": return Vector2.Min(lhs, rhs)
  @staticmethod
  def MoveTowards(current:"Vector2", target:"Vector2", maxDistanceDelta:float) -> "Vector2": return Vector2.MoveTowards(current, target, maxDistanceDelta)
  def Normalize(self) -> None: self.Normalize()
  @staticmethod
  def Perpendicular(inDirection:"Vector2") -> "Vector2": return Vector2.Perpendicular(inDirection)
  @staticmethod
  def Reflect(inDirection:"Vector2", inNormal:"Vector2") -> "Vector2": return Vector2.Reflect(inDirection, inNormal)
  @staticmethod
  def Scale(a:"Vector2", b:"Vector2") -> "Vector2": return Vector2.Scale(a, b)
  def Scale(self, scale:"Vector2") -> None: self.Scale(scale)
  def Set(self, newX:float, newY:float) -> None: self.Set(newX, newY)
  @staticmethod
  def SignedAngle(_from:"Vector2", to:"Vector2") -> float: return Vector2.SignedAngle(_from, to)
  @staticmethod
  def SmoothDamp(current:"Vector2", target:"Vector2", currentVelocity:object, smoothTime:float, maxSpeed:float) -> "Vector2": return Vector2.SmoothDamp(current, target, currentVelocity, smoothTime, maxSpeed)
  @staticmethod
  def SmoothDamp(current:"Vector2", target:"Vector2", currentVelocity:object, smoothTime:float) -> "Vector2": return Vector2.SmoothDamp(current, target, currentVelocity, smoothTime)
  @staticmethod
  def SmoothDamp(current:"Vector2", target:"Vector2", currentVelocity:object, smoothTime:float, maxSpeed:float, deltaTime:float) -> "Vector2": return Vector2.SmoothDamp(current, target, currentVelocity, smoothTime, maxSpeed, deltaTime)
  @staticmethod
  def SqrMagnitude(a:"Vector2") -> float: return Vector2.SqrMagnitude(a)
  def SqrMagnitude(self) -> float: return self.SqrMagnitude()
  def ToString(self) -> str: return self.ToString()
  def ToString(self, format:str) -> str: return self.ToString(format)
  def ToString(self, format:str, formatProvider:object) -> str: return self.ToString(format, formatProvider)
class TextAlign():
  def __init__(self):
    self.value__:int = None
    TopLeft:"int" = None
    Top:"int" = None
    TopRight:"int" = None
    TopJustified:"int" = None
    TopFlush:"int" = None
    TopGeoAligned:"int" = None
    Left:"int" = None
    Center:"int" = None
    Right:"int" = None
    Justified:"int" = None
    Flush:"int" = None
    CenterGeoAligned:"int" = None
    BottomLeft:"int" = None
    Bottom:"int" = None
    BottomRight:"int" = None
    BottomJustified:"int" = None
    BottomFlush:"int" = None
    BottomGeoAligned:"int" = None
    BaselineLeft:"int" = None
    Baseline:"int" = None
    BaselineRight:"int" = None
    BaselineJustified:"int" = None
    BaselineFlush:"int" = None
    BaselineGeoAligned:"int" = None
    MidlineLeft:"int" = None
    Midline:"int" = None
    MidlineRight:"int" = None
    MidlineJustified:"int" = None
    MidlineFlush:"int" = None
    MidlineGeoAligned:"int" = None
    CaplineLeft:"int" = None
    Capline:"int" = None
    CaplineRight:"int" = None
    CaplineJustified:"int" = None
    CaplineFlush:"int" = None
    CaplineGeoAligned:"int" = None
    Converted:"int" = None
  def CompareTo(self, target:object) -> int: return self.CompareTo(target)
  def Equals(self, obj:object) -> bool: return self.Equals(obj)
  def GetHashCode(self) -> int: return self.GetHashCode()
  def GetTypeCode(self) -> int: return self.GetTypeCode()
  def HasFlag(self, flag:object) -> bool: return self.HasFlag(flag)
  def ToString(self) -> str: return self.ToString()
  def ToString(self, format:str, provider:object) -> str: return self.ToString(format, provider)
  def ToString(self, format:str) -> str: return self.ToString(format)
  def ToString(self, provider:object) -> str: return self.ToString(provider)
class OverlayerText():
  def __init__(self):
    self.LineSpacing:float = None
    self.LineSpacingAdjustment:float = None
    self.Active:bool = None
    self.IsExpanded:bool = None
    self.Gradient:bool = None
    self.DisableUpdate:bool = None
    self.Font:str = None
    self.Name:str = None
    self.PlayingText:str = None
    self.NotPlayingText:str = None
    self.Position:Vector2 = None
    self.FontSize:float = None
    self.Alignment:int = None
    self.TextColor:GradientColor = None
    self.ShadowColor:GradientColor = None
  def Apply(self) -> None: self.Apply()
  def GetShadowColor(self) -> Color: return self.GetShadowColor()
  def GetTextColor(self) -> Color: return self.GetTextColor()
  def SetShadowColor(self, color:Color) -> Color: return self.SetShadowColor(color)
  def SetTextColor(self, color:Color) -> None: self.SetTextColor(color)
  def Update(self) -> None: self.Update()
class TileInfo():
  def __init__(self):
    self.Accuracy:float = None
    self.XAccuracy:float = None
    self.SeqID:int = None
    self.Timing:float = None
    self.TimingAvg:float = None
    self.Bpm:float = None
    self.HitMargin:int = None
  def ToString(self) -> str: return self.ToString()
class Interop():
  def __init__(self):
    pass
  @staticmethod
  def ExportPyFunction(name:str, func:object) -> None: Interop.ExportPyFunction(name, func)
  @staticmethod
  def InvokeCJSFunction(name:str, args:list) -> object: return Interop.InvokeCJSFunction(name, args)
  @staticmethod
  def InvokeJSFunction(name:str, args:list) -> object: return Interop.InvokeJSFunction(name, args)
class CompiledJS():
  def __init__(self):
    pass
  def Evaluate(self) -> object: return self.Evaluate()
  def EvaluateWith(self, withEval:"CompiledJS") -> object: return self.EvaluateWith(withEval)
  def Execute(self) -> None: self.Execute()
  def ExecuteWith(self, withExec:"CompiledJS") -> None: self.ExecuteWith(withExec)
class TextCompiler():
  def __init__(self):
    pass
  def Compile(self, str:str) -> None: self.Compile(str)
  @staticmethod
  def Create() -> "TextCompiler": return TextCompiler.Create()
  def GetValue(self) -> str: return self.GetValue()
def RegisterTagOpt(name:str, func:object, notplaying:bool) -> None:
    RegisterTagOpt(name, func, notplaying)
def RegisterTag(name:str, func:object, notplaying:bool) -> None:
    RegisterTag(name, func, notplaying)
def UnregisterTag(name:str) -> None:
    UnregisterTag(name)
def Log(obj:object) -> None:
    Log(obj)
def ToString(obj:object) -> str:
    return ToString(obj)
def GetGlobalVariable(name:str) -> object:
    return GetGlobalVariable(name)
def SetGlobalVariable(name:str, obj:object) -> object:
    return SetGlobalVariable(name, obj)
def RoundFloat(value:float, digits:int) -> float:
    return RoundFloat(value, digits)
def RoundFloatString(value:float, digits:int) -> str:
    return RoundFloatString(value, digits)
def GetText(index:int) -> OverlayerText:
    return GetText(index)
def RainbowColor(speed:float) -> Color:
    return RainbowColor(speed)
def Compile(source:str) -> CompiledJS:
    """
    Compile Javascript From Source\n
    !!Warning!! Javascript Compilation May Leak Memory!
    """
    return Compile(source)
def CompileFile(path:str) -> CompiledJS:
    """
    Compile Javascript From File\n
    !!Warning!! Javascript Compilation May Leak Memory!
    """
    return CompileFile(path)
def GetTileInfos() -> list:
    return GetTileInfos()
