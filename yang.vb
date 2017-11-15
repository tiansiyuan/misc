Imports System
    
Public Module Module1
 Public Sub Main()
  
  Dim Calculator(50) As Char
  'The string of numbers and symbols that the user inputs
  Dim numExt1(50) As Integer
  Dim numExt2(50) As Integer
  'Number transferring
  Dim i,j As Integer
  'The iterator
  Dim mark As Integer
  Dim mark2 As Integer = 0
  'The extract of each digit
  Dim ope As Char
  Dim opeSym As Integer
  'The calculation operator storage
  Dim num1 As Double = 0
  Dim num2 As Double = 0
  'Two numbers for each calculation
  Dim Answer As Double = 0
  'The result of calculation
  
  Console.Writeline("Please enter a string of numbers and operations: ")
  Calculator(50) = Console.Readline()
  
  For i = 0 To Calculator.Length-1
  If Char.IsDigit(Calculator(i)) = true Then
   mark = i 
  ElseIf Char.IsDigit(Calculator(i)) = false Then
   
   If Calculator(i) <> "=" Then
    ope = Calculator(i)
    Select Case ope
    Case "+"
     opeSym = 1
    Case "-"
     opeSym = 2
    Case "*"
     opeSym = 3
    Case "/"
     opeSym = 4
    End Select
   ElseIf Calculator(i) = "=" Then
    Console.Writeline(Answer)
    Exit For
   End If
   
   If num1 = 0 Then
    For j = mark2 To mark
    numExt1(j) = Microsoft.VisualBasic.Val(Calculator(j))
    num1 = num1 + numExt1(j) * 10^(mark-j)
    Next
   mark2 = i + 1
   Else
    For j = mark2 To mark
    numExt2(j) = Microsoft.VisualBasic.Val(Calculator(j))
    num2 = num2 +  numExt2(j) * 10^(mark-j)
    If Answer = 0 Then
     Select Case opeSym
     Case 1
     Answer = num1 + num2
     Case 2
     Answer = num1 - num2
     Case 3
     Answer = num1 * num2
     Case 4
     Answer = num1 / num2
     End Select
    Else
     Select Case opeSym
     Case 1
     Answer = Answer + num2
     Case 2
     Answer = Answer - num2
     Case 3
     Answer = Answer * num2
     Case 4
     Answer = Answer / num2
     End Select
    End If
   mark2 = i + 1
    Next
  
   End If
  
  Else 
   Console.Writeline("You typed in something unrecognisable!")
  End If
  Next
 End Sub
End Module
