import { useTranslation } from 'react-i18next';
import { useMediaQuery } from 'react-responsive';

import { menuItems } from 'shared/consts';

const useGetMenuItems = (role?: UserRole) => {
  const { t } = useTranslation();
  const isDesktop = useMediaQuery({ minWidth: 910 });

  let currentMenuItems = isDesktop ? menuItems.filter((item) => item.key !== 'profile') : menuItems;

  if (role === 'USER') {
    currentMenuItems = menuItems.filter((item) => item.key !== 'schedule');
  } else {
    currentMenuItems = menuItems.filter((item) => item.key !== 'cars');
  }

  return currentMenuItems.map((item) => ({ ...item, label: t(item.label) }));
};

export default useGetMenuItems;
