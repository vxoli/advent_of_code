
function read_int_list(file_name) result(list)
        character(*), intent(in) :: file_name
        integer, allocatable :: list(:)
        integer :: i, file_len

        open(unit=15, file=file_name, status="old", action="read")

        file_len = count_file_lines(15)
        
        allocate(list(file_len))
        
        do i = 1, file_len
            read(15, *) list(i)
        end do

        close(15)
    end function

function count_file_lines(unit) result(line_count)
        integer, intent(in) :: unit
        integer :: line_count, stat

        line_count = 0
        do
            read(unit, "(a)", iostat=stat)
            if (stat /= 0) exit
            line_count = line_count + 1
        end do
        
        rewind(unit)
    end function count_file_lines


program day_01

!
! Read Data
!

integer, allocatable :: list(:)
integer :: i, j, k

list = read_int_list("d01p1-input.txt")
!
! Part 1
!
outer: do i = 1, size(list)-1
	do j = i+1,size(list)
		if(list(i) + list(j) == 2020) then
			print'("Part 1 answer: ", I0)', list(i) * list(j)
			exit outer
		end if
	end do
end do outer

end program day_01