'use client';
import * as React from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { styled, alpha } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import InputBase from '@mui/material/InputBase';
import SearchIcon from '@mui/icons-material/Search';
import { useRouter } from 'next/navigation'; // Import useRouter hook

const Search = styled('div')(({ theme }) => ({
  position: 'relative',
  borderRadius: theme.shape.borderRadius,
  backgroundColor: alpha(theme.palette.common.white, 0.15),
  '&:hover': {
    backgroundColor: alpha(theme.palette.common.white, 0.25),
  },
  marginLeft: 0,
  width: '100%',
  [theme.breakpoints.up('sm')]: {
    marginLeft: theme.spacing(1),
    width: 'auto',
  },
}));

const SearchIconWrapper = styled('div')(({ theme }) => ({
  padding: theme.spacing(0, 2),
  height: '100%',
  position: 'absolute',
  pointerEvents: 'none',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
}));

const StyledInputBase = styled(InputBase)(({ theme }) => ({
  color: 'inherit',
  width: '100%',
  '& .MuiInputBase-input': {
    padding: theme.spacing(1, 1, 1, 0),
    paddingLeft: `calc(1em + ${theme.spacing(4)})`,
    transition: theme.transitions.create('width'),
    [theme.breakpoints.up('sm')]: {
      width: '13ch',
      '&:focus': {
        width: '20ch',
      },
    },
  },
}));

function SearchAppBar() {
  const router = useRouter();

  const handleSearchSubmit = (event) => {
    event.preventDefault();
    const searchQuery = event.target.search.value;
    console.log(searchQuery);
    router.push(`/lifters/${searchQuery}`);
  };

  
  return (
    <Box sx={{ flexGrow: 1 }} >
      <AppBar position="static" sx={{ bgcolor: '#F83315' }}>
        <Toolbar>
          <Link href='/home'>
            <Image src="/openstatlogo.png" alt="OpenStat Logo" width={75} height={75} />
          </Link>
          <Typography variant="h6" noWrap component="div" sx={{ flexGrow: 1, display: { xs: 'none', sm: 'block' } }}></Typography>
          {/* Wrap the Search component in a form tag or ensure it renders as a form */}
          <form onSubmit={handleSearchSubmit}>
            <Search>
              <SearchIconWrapper>
                <SearchIcon />
              </SearchIconWrapper>
              <StyledInputBase
                name="name"
                placeholder="Search Lifters..."
                inputProps={{ 'aria-label': 'search' }}
              />
            </Search>
          </form>
        </Toolbar>
      </AppBar>
      
    </Box>
    
  );
}

export default SearchAppBar;