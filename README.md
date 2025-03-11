this probably will not get worked on too much longer
I realized that the following sed oneliner would work pretty much just as well:

```sed
# The p (print) command is typically used together with the -n
# command-line option, which disables the print by default functionality.
# Output all lines between ``` and ```.
/```/,/```/p
```

Source: Learn Sed in Y Minutes
