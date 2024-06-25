import { FC } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import y, { useMediaQuery } from 'react-responsive';
import { observer } from 'mobx-react-lite';
import { useTranslation } from 'react-i18next';

import { useStore } from 'app/store';
import { ThemeSwitcher } from 'features';

import { Image, Layout, Menu, Space } from 'antd';
import { useGetMenuItems } from 'shared/hooks';

import logo from 'shared/img/logo.png';
import { AuthOrProfileButtons } from './auth-or-profile-buttons';

const Header: FC = () => {
  const { pathname } = useLocation();
  const navigate = useNavigate();
  const { t } = useTranslation();

  const { auth, profile } = useStore();

  const isDesktop = useMediaQuery({ minWidth: 911 });

  const menuItems = useGetMenuItems(profile.profile?.role);

  return (
    <Layout.Header className="header">
      <Link to="/" style={{ backgroundColor: '#fff' }}>
        <Image
          src={logo}
          alt="logo"
          width={isDesktop ? 160 : 120}
          height={isDesktop ? 40 : 30}
          preview={false}
        />
      </Link>
      {auth.isAuth && isDesktop && (
        <Menu
          items={menuItems}
          selectedKeys={[pathname]}
          onClick={(e) => navigate(e.key)}
          mode="horizontal"
          className="menu"
        />
      )}
      <Space size="large">
        {isDesktop && <ThemeSwitcher />}
        <AuthOrProfileButtons isAuth={auth.isAuth} isDesktop={isDesktop} />{' '}
      </Space>
    </Layout.Header>
  );
};

export default observer(Header);
