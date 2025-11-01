      double precision function d1mach(i)
c
c  Machine-dependent constants for double precision.
c  Simplified version using Fortran intrinsics.
c
      integer i
      double precision deps, dtiny, dhuge

      deps = epsilon(1.0d0)
      dtiny = tiny(1.0d0)
      dhuge = huge(1.0d0)

      if (i .eq. 1) then
c       Smallest positive magnitude
        d1mach = dtiny
      else if (i .eq. 2) then
c       Largest magnitude
        d1mach = dhuge
      else if (i .eq. 3) then
c       Smallest relative spacing
        d1mach = deps / 2.0d0
      else if (i .eq. 4) then
c       Largest relative spacing
        d1mach = deps
      else if (i .eq. 5) then
c       log10(radix)
        d1mach = dlog10(2.0d0)
      else
        d1mach = 0.0d0
      endif

      return
      end
