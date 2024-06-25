import { FC } from 'react';
import { useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';

import { Button, Flex } from 'antd';
import { AuthModal, Logout, MobileMenu } from 'features';

type AuthOrProfileButtonsProps = { isAuth: boolean; isDesktop: boolean };

export const AuthOrProfileButtons: FC<AuthOrProfileButtonsProps> = ({ isAuth, isDesktop }) => {
  const navigate = useNavigate();
  const { t } = useTranslation();

  if (!isAuth) return <AuthModal />;

  if (isDesktop) {
    return (
      <Flex gap={20}>
        <Button type="primary" onClick={() => navigate('profile')}>
          {t('Profile')}
        </Button>
        <Logout />
      </Flex>
    );
  }

  return <MobileMenu />;
};
