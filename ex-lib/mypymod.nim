import nimpy

proc say_hi(arg:string):string {.exportpy.} =
    return "Hello " & arg

