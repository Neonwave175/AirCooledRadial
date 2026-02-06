@echo off
REM init script
IF "%~1" "=" "-ssr" (
  echo "Schwarzschild Radius Finder"
  python3 "SchwarzschildRadiusFinder.py"
) ELSE (
  IF "%~1" "=" "-emcs" (
    echo "Energy Mass Equation"
    python3 "EnergyMassEquation.py"
  ) ELSE (
    IF "%~1" "=" "-tvel" (
      echo "Terminal Velocity Finder"
      python3 "TerminalVelocityFinder.py"
    ) ELSE (
      IF "%~1" "=" "-help" (
        echo "--Help--"
        echo ""
        echo "-ssr for Schwarzschild Radius Finder, -emcs for Energy Mass Equation, -tvel for Terminal Velocity Finder"
      ) ELSE (
        echo "Unknown command, type -help for list of commands"
      )
    )
  )
)
