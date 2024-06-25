type MenuKeys = '/' | 'schedule' | 'cars' | 'profile';

type MenuItems = {
  label: string;
  key: MenuKeys;
};

export const menuItems: MenuItems[] = [
  {
    label: 'Home',
    key: '/',
  },
  {
    label: 'Profile',
    key: 'profile',
  },
  {
    label: 'Schedule',
    key: 'schedule',
  },
  {
    label: 'Cars',
    key: 'cars',
  },
];
