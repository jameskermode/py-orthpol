      real function r1mach(i)
c
c  Machine-dependent constants for single precision.
c  Simplified version using Fortran intrinsics.
c
      integer i
      real eps, rtiny, rhuge

      eps = epsilon(1.0)
      rtiny = tiny(1.0)
      rhuge = huge(1.0)

      if (i .eq. 1) then
c       Smallest positive magnitude
        r1mach = rtiny
      else if (i .eq. 2) then
c       Largest magnitude
        r1mach = rhuge
      else if (i .eq. 3) then
c       Smallest relative spacing
        r1mach = eps / 2.0
      else if (i .eq. 4) then
c       Largest relative spacing
        r1mach = eps
      else if (i .eq. 5) then
c       log10(radix)
        r1mach = alog10(2.0)
      else
        r1mach = 0.0
      endif

      return
      end
