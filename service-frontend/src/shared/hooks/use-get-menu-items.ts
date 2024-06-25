import { useTranslation } from 'react-i18next';

import { menuItems } from 'shared/consts';
import useMedia from './use-media';

const useGetMenuItems = (role?: UserRole) => {
  const { t } = useTranslation();
  const { isDesktop } = useMedia();

  let currentMenuItems = isDesktop ? menuItems.filter((item) => item.key !== 'profile') : menuItems;

  if (role === 'USER') {
    currentMenuItems = currentMenuItems.filter((item) => item.key !== 'schedule');
  } else {
    currentMenuItems = currentMenuItems.filter((item) => item.key !== 'cars');
  }

  return currentMenuItems.map((item) => ({ ...item, label: t(item.label) }));
};

export default useGetMenuItems;
